import pygame
import sys
import math
import os
import json

pygame.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sew Far Sew Good - Prototype")

clock = pygame.time.Clock()
FPS = 60

# ============================================================
# ASSETS
# ============================================================

DEFAULT_TARGET_WIDTH = 160

CHARACTER_FILENAMES = ["character1.png", "character2.png", "character3.png", "character4.png",
                        "character5.png", "character6.png", "character7.png", "character8.png",
                        "character9.png", "character10.png"]

CHARACTER_WIDTH_OVERRIDES = {
    4: 200,
    5: 200,
    6: 200,
    7: 200,
    8: 200,
    9: 200,
}

character_images = []
character_images_raw = []

for index, filename in enumerate(CHARACTER_FILENAMES):
    path = os.path.join(BASE_DIR, "assets", "characters", filename)
    raw_image = pygame.image.load(path).convert_alpha()
    character_images_raw.append(raw_image)

    original_width = raw_image.get_width()
    original_height = raw_image.get_height()

    target_width_for_this_character = CHARACTER_WIDTH_OVERRIDES.get(index, DEFAULT_TARGET_WIDTH)
    raw_scale = target_width_for_this_character / original_width

    if raw_scale >= 1:
        # Enlarging a small image — round to a whole number for crisp pixel art
        clean_scale = max(1, round(raw_scale))
        target_width = original_width * clean_scale
        target_height = original_height * clean_scale
        scaled_image = pygame.transform.scale(raw_image, (target_width, target_height))
    else:
        # Shrinking a large image — scale down directly, smoothly
        target_width = target_width_for_this_character
        target_height = int(original_height * raw_scale)
        scaled_image = pygame.transform.smoothscale(raw_image, (target_width, target_height))

    character_images.append(scaled_image)

selected_character_index = 0
player_image_original = character_images[selected_character_index]
player_rect = player_image_original.get_rect()
player_rect.center = (150, 250)
player_speed = 5
menu_background = pygame.image.load(os.path.join(BASE_DIR, "assets", "menu_background.png")).convert()
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

characters_background = pygame.image.load(os.path.join(BASE_DIR, "assets", "characters_background.png")).convert()
characters_background = pygame.transform.scale(characters_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

fabrics_background = pygame.image.load(os.path.join(BASE_DIR, "assets", "fabrics_background.png")).convert()
fabrics_background = pygame.transform.scale(fabrics_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

shapes_background = pygame.image.load(os.path.join(BASE_DIR, "assets", "shapes_background.png")).convert()
shapes_background = pygame.transform.scale(shapes_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

FABRIC_FILENAMES = ["fabric1.png", "fabric2.png", "fabric3.png", "fabric4.png", "fabric5.png", "fabric6.png", "fabric7.png"]
fabric_images = []
for filename in FABRIC_FILENAMES:
    path = os.path.join(BASE_DIR, "assets", "fabrics", filename)
    fabric_images.append(pygame.image.load(path).convert())

selected_fabric_index = 0
background_tile = fabric_images[selected_fabric_index]
tile_width = background_tile.get_width()
tile_height = background_tile.get_height()

facing_right = True
is_moving = False
walk_timer = 0

# ============================================================
# STITCH TEMPLATE SETUP
# ============================================================

template_center = (500, 250)
template_radius = 150
NUM_STITCHES = 10
STITCH_CATCH_RADIUS = 30

stitched = [False] * NUM_STITCHES
current_target = 0

TIME_LIMIT_SECONDS = 60
start_ticks = None

font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "MyFont.ttf"), 36)
title_font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "MyFont.ttf"), 64)
game_over = False
score_already_saved = False
final_message = ""
time_left = TIME_LIMIT_SECONDS

POINTS_PER_STITCH = 80
TIME_BONUS_MULTIPLIER = 5
final_score = 0

player_name_input = ""
entering_name = False
MAX_NAME_LENGTH = 12

current_screen = "menu"  # "menu" -> "game" / "characters" / "fabrics" / "shapes"

# ============================================================
# LAYOUT CONSTANTS (thumbnails + scrolling)
# ============================================================
FABRIC_THUMB_SIZE = 120
CHARACTER_THUMB_SIZE = 180
THUMB_GAP = 30
THUMBS_PER_ROW = 3

SCROLL_SPEED = 30
SCROLL_AREA_TOP = 200
SCROLL_AREA_BOTTOM = SCREEN_HEIGHT - 100
scroll_area_rect = pygame.Rect(0, SCROLL_AREA_TOP, SCREEN_WIDTH, SCROLL_AREA_BOTTOM - SCROLL_AREA_TOP)

fabric_scroll_offset = 0
character_scroll_offset = 0

# ============================================================
# BUTTONS
# ============================================================

play_button = pygame.Rect(0, 0, 200, 60)
play_button.center = (SCREEN_WIDTH // 2, 260)

characters_button = pygame.Rect(0, 0, 200, 60)
characters_button.center = (SCREEN_WIDTH // 2, 320)

fabrics_button = pygame.Rect(0, 0, 200, 60)
fabrics_button.center = (SCREEN_WIDTH // 2, 380)

shapes_button = pygame.Rect(0, 0, 200, 60)
shapes_button.center = (SCREEN_WIDTH // 2, 440)

quit_button = pygame.Rect(0, 0, 200, 60)
quit_button.center = (SCREEN_WIDTH // 2, 500)

back_button = pygame.Rect(0, 0, 200, 60)
back_button.center = (SCREEN_WIDTH // 2, 570)

play_again_button = pygame.Rect(0, 0, 200, 60)
play_again_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)

back_to_menu_button = pygame.Rect(0, 0, 200, 60)
back_to_menu_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130)

game_back_button = pygame.Rect(0, 0, 120, 50)
game_back_button.topleft = (20, 20)

pause_button = pygame.Rect(0, 0, 120, 50)
pause_button.topleft = (SCREEN_WIDTH - 140, 20)

resume_button = pygame.Rect(0, 0, 200, 60)
resume_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

paused = False
pause_start_tick = None

# ============================================================
# THUMBNAIL GRIDS (fabrics + characters)
# ============================================================

fabric_thumb_rects = []
row_width = THUMBS_PER_ROW * FABRIC_THUMB_SIZE + (THUMBS_PER_ROW - 1) * THUMB_GAP
start_x = (SCREEN_WIDTH - row_width) // 2
for index in range(len(fabric_images)):
    row = index // THUMBS_PER_ROW
    col = index % THUMBS_PER_ROW
    rect = pygame.Rect(0, 0, FABRIC_THUMB_SIZE, FABRIC_THUMB_SIZE)
    rect.topleft = (start_x + col * (FABRIC_THUMB_SIZE + THUMB_GAP), 220 + row * (FABRIC_THUMB_SIZE + THUMB_GAP))
    fabric_thumb_rects.append(rect)

fabric_rows = (len(fabric_images) + THUMBS_PER_ROW - 1) // THUMBS_PER_ROW
fabric_content_height = fabric_rows * FABRIC_THUMB_SIZE + (fabric_rows - 1) * THUMB_GAP
fabric_max_scroll = max(0, fabric_content_height - scroll_area_rect.height)

CHARACTER_THUMBS_PER_ROW = 2  # NEW: separate from fabric's row count, since these are bigger

character_thumb_rects = []
char_row_width = CHARACTER_THUMBS_PER_ROW * CHARACTER_THUMB_SIZE + (CHARACTER_THUMBS_PER_ROW - 1) * THUMB_GAP
char_start_x = (SCREEN_WIDTH - char_row_width) // 2
for index in range(len(character_images)):
    row = index // CHARACTER_THUMBS_PER_ROW
    col = index % CHARACTER_THUMBS_PER_ROW
    rect = pygame.Rect(0, 0, CHARACTER_THUMB_SIZE, CHARACTER_THUMB_SIZE)
    rect.topleft = (char_start_x + col * (CHARACTER_THUMB_SIZE + THUMB_GAP), 220 + row * (CHARACTER_THUMB_SIZE + THUMB_GAP))
    character_thumb_rects.append(rect)

character_rows = (len(character_images) + CHARACTER_THUMBS_PER_ROW - 1) // CHARACTER_THUMBS_PER_ROW
character_content_height = character_rows * CHARACTER_THUMB_SIZE + (character_rows - 1) * THUMB_GAP
character_max_scroll = max(0, character_content_height - scroll_area_rect.height)

# ============================================================
# FUNCTIONS
# ============================================================

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def points_on_polygon_perimeter(vertices, num_points):
    edge_lengths = []
    for i in range(len(vertices)):
        start = vertices[i]
        end = vertices[(i + 1) % len(vertices)]
        edge_lengths.append(distance(start, end))

    total_perimeter = sum(edge_lengths)
    spacing = total_perimeter / num_points

    points = []
    for i in range(num_points):
        target_distance = i * spacing
        accumulated = 0
        current_edge = 0
        distance_into_edge = 0
        for edge_index in range(len(edge_lengths)):
            if accumulated + edge_lengths[edge_index] >= target_distance:
                current_edge = edge_index
                distance_into_edge = target_distance - accumulated
                break
            accumulated += edge_lengths[edge_index]

        start = vertices[current_edge]
        end = vertices[(current_edge + 1) % len(vertices)]
        edge_length = edge_lengths[current_edge]

        t = distance_into_edge / edge_length if edge_length > 0 else 0
        x = start[0] + (end[0] - start[0]) * t
        y = start[1] + (end[1] - start[1]) * t
        points.append((x, y))

    return points


def get_square_vertices(center, size):
    half = size / 2
    return [
        (center[0] - half, center[1] - half),
        (center[0] + half, center[1] - half),
        (center[0] + half, center[1] + half),
        (center[0] - half, center[1] + half),
    ]


def get_triangle_vertices(center, size):
    return [
        (center[0], center[1] - size),
        (center[0] + size * 0.87, center[1] + size * 0.5),
        (center[0] - size * 0.87, center[1] + size * 0.5),
    ]


def get_star_vertices(center, size, points=5):
    vertices = []
    outer_radius = size
    inner_radius = size * 0.45
    for i in range(points * 2):
        angle = (math.pi / points) * i - math.pi / 2
        radius = outer_radius if i % 2 == 0 else inner_radius
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        vertices.append((x, y))
    return vertices


def generate_stitch_points(shape_name, center, size, num_points):
    if shape_name == "circle":
        pts = []
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            x = center[0] + size * math.cos(angle)
            y = center[1] + size * math.sin(angle)
            pts.append((x, y))
        return pts
    elif shape_name == "square":
        return points_on_polygon_perimeter(get_square_vertices(center, size), num_points)
    elif shape_name == "triangle":
        return points_on_polygon_perimeter(get_triangle_vertices(center, size), num_points)
    elif shape_name == "star":
        return points_on_polygon_perimeter(get_star_vertices(center, size), num_points)


def draw_button(rect, text, hovered):
    color = (160, 20, 20) if hovered else (120, 10, 10)
    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), rect, width=3, border_radius=10)
    label = font.render(text, True, (255, 255, 255))
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

SCORE_FILE = os.path.join(BASE_DIR, "scores.json")

def load_scores():
    if not os.path.exists(SCORE_FILE):
        return []
    with open(SCORE_FILE, "r") as f:
        return json.load(f)

def save_score(name, score):
    scores = load_scores()
    scores.append({"name": name, "score": score})  # NEW: a dictionary instead of a bare number
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f)

# ============================================================
# SHAPE SELECTION SETUP (uses functions defined above)
# ============================================================

SHAPE_NAMES = ["circle", "square", "triangle", "star"]
selected_shape_index = 0
stitch_points = generate_stitch_points(SHAPE_NAMES[selected_shape_index], template_center, template_radius, NUM_STITCHES)

shape_thumb_rects = []
shape_row_width = len(SHAPE_NAMES) * FABRIC_THUMB_SIZE + (len(SHAPE_NAMES) - 1) * THUMB_GAP
shape_start_x = (SCREEN_WIDTH - shape_row_width) // 2
for index in range(len(SHAPE_NAMES)):
    rect = pygame.Rect(0, 0, FABRIC_THUMB_SIZE, FABRIC_THUMB_SIZE)
    rect.topleft = (shape_start_x + index * (FABRIC_THUMB_SIZE + THUMB_GAP), 220)
    shape_thumb_rects.append(rect)

# ============================================================
# MAIN LOOP
# ============================================================

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_screen == "menu":
                if play_button.collidepoint(mouse_pos):
                    current_screen = "game"
                    start_ticks = pygame.time.get_ticks()
                    stitched = [False] * NUM_STITCHES
                    current_target = 0
                    game_over = False
                    final_message = ""
                    final_score = 0
                    score_history = load_scores()
                    score_already_saved = False  # NEW: prevents saving the same score repeatedly every frame
                    player_rect.center = (150, 250)
                elif characters_button.collidepoint(mouse_pos):
                    current_screen = "characters"
                elif fabrics_button.collidepoint(mouse_pos):
                    current_screen = "fabrics"
                elif shapes_button.collidepoint(mouse_pos):
                    current_screen = "shapes"
                elif quit_button.collidepoint(mouse_pos):
                    running = False

            elif current_screen == "characters":
                if back_button.collidepoint(mouse_pos):
                    current_screen = "menu"
                else:
                    for index, rect in enumerate(character_thumb_rects):
                        draw_rect = rect.move(0, -character_scroll_offset)
                        if draw_rect.collidepoint(mouse_pos):
                            selected_character_index = index
                            player_image_original = character_images[selected_character_index]
                            player_rect = player_image_original.get_rect(center=player_rect.center)

            elif current_screen == "fabrics":
                if back_button.collidepoint(mouse_pos):
                    current_screen = "menu"
                else:
                    for index, rect in enumerate(fabric_thumb_rects):
                        draw_rect = rect.move(0, -fabric_scroll_offset)
                        if draw_rect.collidepoint(mouse_pos):
                            selected_fabric_index = index
                            background_tile = fabric_images[selected_fabric_index]
                            tile_width = background_tile.get_width()
                            tile_height = background_tile.get_height()

            elif current_screen == "shapes":
                if back_button.collidepoint(mouse_pos):
                    current_screen = "menu"
                else:
                    for index, rect in enumerate(shape_thumb_rects):
                        if rect.collidepoint(mouse_pos):
                            selected_shape_index = index
                            stitch_points = generate_stitch_points(
                                SHAPE_NAMES[selected_shape_index], template_center, template_radius, NUM_STITCHES
                            )
                            stitched = [False] * NUM_STITCHES
                            current_target = 0

            elif current_screen == "game" and not game_over:
                if game_back_button.collidepoint(mouse_pos):
                    current_screen = "menu"
                    paused = False
                elif pause_button.collidepoint(mouse_pos) and not paused:
                    paused = True
                    pause_start_tick = pygame.time.get_ticks()
                elif paused and resume_button.collidepoint(mouse_pos):
                    paused_duration = pygame.time.get_ticks() - pause_start_tick
                    start_ticks += paused_duration
                    paused = False

            elif current_screen == "game" and game_over:
                if play_again_button.collidepoint(mouse_pos):
                    stitched = [False] * NUM_STITCHES
                    current_target = 0
                    game_over = False
                    final_message = ""
                    final_score = 0
                    start_ticks = pygame.time.get_ticks()
                    player_rect.center = (150, 250)
                elif back_to_menu_button.collidepoint(mouse_pos):
                    current_screen = "menu"

        if event.type == pygame.MOUSEWHEEL:
            if current_screen == "fabrics":
                fabric_scroll_offset -= event.y * SCROLL_SPEED
                fabric_scroll_offset = max(0, min(fabric_scroll_offset, fabric_max_scroll))
            elif current_screen == "characters":
                character_scroll_offset -= event.y * SCROLL_SPEED
                character_scroll_offset = max(0, min(character_scroll_offset, character_max_scroll))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if current_screen == "game" and not game_over:
                if current_target < NUM_STITCHES:
                    target_pos = stitch_points[current_target]
                    if distance(player_rect.center, target_pos) <= STITCH_CATCH_RADIUS:
                        stitched[current_target] = True
                        current_target += 1
        if event.type == pygame.KEYDOWN and entering_name:
            print("Key event received:", event.unicode, "| current input:", player_name_input)  # TEMP DEBUG
            if event.key == pygame.K_RETURN:
                name_to_save = player_name_input.strip() if player_name_input.strip() != "" else "Anonymous"
                save_score(name_to_save, final_score)
                entering_name = False
            elif event.key == pygame.K_BACKSPACE:
                player_name_input = player_name_input[:-1]
            else:
                if len(player_name_input) < MAX_NAME_LENGTH and event.unicode.isprintable():
                    player_name_input += event.unicode

    # ============================================================
    # MENU SCREEN
    # ============================================================
    if current_screen == "menu":
        screen.blit(menu_background, (0, 0))
        title_text = title_font.render("Sew you up", True, (255, 240, 220))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        screen.blit(title_text, title_rect)

        draw_button(play_button, "Play", play_button.collidepoint(mouse_pos))
        draw_button(characters_button, "Characters", characters_button.collidepoint(mouse_pos))
        draw_button(fabrics_button, "Fabrics", fabrics_button.collidepoint(mouse_pos))
        draw_button(shapes_button, "Shapes", shapes_button.collidepoint(mouse_pos))
        draw_button(quit_button, "Quit", quit_button.collidepoint(mouse_pos))

    # ============================================================
    # CHARACTERS SCREEN
    # ============================================================
    elif current_screen == "characters":
        screen.blit(characters_background, (0, 0))
        label = title_font.render("Choose a Character", True, (255, 240, 220))
        screen.blit(label, label.get_rect(center=(SCREEN_WIDTH // 2, 130)))

        screen.set_clip(scroll_area_rect)
        for index, rect in enumerate(character_thumb_rects):
            draw_rect = rect.move(0, -character_scroll_offset)
            thumb = pygame.transform.scale(character_images_raw[index], (CHARACTER_THUMB_SIZE, CHARACTER_THUMB_SIZE))
            screen.blit(thumb, draw_rect)

            if index == selected_character_index:
                pygame.draw.rect(screen, (255, 220, 0), draw_rect, width=4)
            elif draw_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 255), draw_rect, width=3)
            else:
                pygame.draw.rect(screen, (30, 30, 30), draw_rect, width=2)
        screen.set_clip(None)

        draw_button(back_button, "Back", back_button.collidepoint(mouse_pos))
        thumb = pygame.transform.scale(character_images_raw[index], (CHARACTER_THUMB_SIZE, CHARACTER_THUMB_SIZE))
    # ============================================================
    # FABRICS SCREEN
    # ============================================================
    elif current_screen == "fabrics":
        screen.blit(fabrics_background, (0, 0))
        label = title_font.render("Choose a Fabric", True, (255, 240, 220))
        screen.blit(label, label.get_rect(center=(SCREEN_WIDTH // 2, 130)))

        screen.set_clip(scroll_area_rect)
        for index, rect in enumerate(fabric_thumb_rects):
            draw_rect = rect.move(0, -fabric_scroll_offset)
            thumb = pygame.transform.scale(fabric_images[index], (FABRIC_THUMB_SIZE, FABRIC_THUMB_SIZE))
            screen.blit(thumb, draw_rect)

            if index == selected_fabric_index:
                pygame.draw.rect(screen, (255, 220, 0), draw_rect, width=4)
            elif draw_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 255), draw_rect, width=3)
            else:
                pygame.draw.rect(screen, (30, 30, 30), draw_rect, width=2)
        screen.set_clip(None)

        draw_button(back_button, "Back", back_button.collidepoint(mouse_pos))

    # ============================================================
    # SHAPES SCREEN
    # ============================================================
    elif current_screen == "shapes":
        screen.blit(shapes_background, (0, 0))
        label = title_font.render("Choose a Shape", True, (255, 240, 220))
        screen.blit(label, label.get_rect(center=(SCREEN_WIDTH // 2, 130)))

        for index, rect in enumerate(shape_thumb_rects):
            preview_center = rect.center
            preview_size = FABRIC_THUMB_SIZE * 0.35
            shape_name = SHAPE_NAMES[index]
            preview_points = generate_stitch_points(shape_name, preview_center, preview_size, 30)
            pygame.draw.polygon(screen, (255, 255, 255), preview_points, width=3)

            if index == selected_shape_index:
                pygame.draw.rect(screen, (255, 220, 0), rect, width=4)
            elif rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 255), rect, width=3)
            else:
                pygame.draw.rect(screen, (30, 30, 30), rect, width=2)

        draw_button(back_button, "Back", back_button.collidepoint(mouse_pos))

    # ============================================================
    # GAME SCREEN
    # ============================================================
    elif current_screen == "game":
        if not game_over and not paused:
            keys = pygame.key.get_pressed()
            dx = 0
            dy = 0
            if keys[pygame.K_w]:
                dy -= player_speed
            if keys[pygame.K_s]:
                dy += player_speed
            if keys[pygame.K_a]:
                dx -= player_speed
            if keys[pygame.K_d]:
                dx += player_speed

            player_rect.x += dx
            player_rect.y += dy
            player_rect.clamp_ip(screen.get_rect())

            is_moving = (dx != 0 or dy != 0)
            if dx < 0:
                facing_right = False
            elif dx > 0:
                facing_right = True

            if is_moving:
                walk_timer += 1
            else:
                walk_timer = 0

            elapsed_seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            time_left = max(0, TIME_LIMIT_SECONDS - elapsed_seconds)

            if current_target >= NUM_STITCHES:
                game_over = True
                final_score = (current_target * POINTS_PER_STITCH) + int(time_left * TIME_BONUS_MULTIPLIER)
                final_message = f"All stitches placed! Score: {final_score}"
                entering_name = True
                player_name_input = ""
            elif time_left <= 0:
                game_over = True
                final_score = current_target * POINTS_PER_STITCH
                final_message = f"Time's up! You stitched {current_target}/{NUM_STITCHES} - Score: {final_score}"
                entering_name = True
                player_name_input = ""
        for x in range(0, SCREEN_WIDTH, tile_width):
            for y in range(0, SCREEN_HEIGHT, tile_height):
                screen.blit(background_tile, (x, y))

        for i, point in enumerate(stitch_points):
            if stitched[i]:
                pygame.draw.circle(screen, (80, 200, 100), point, 8)
            elif i == current_target:
                pygame.draw.circle(screen, (255, 220, 0), point, 10)
            else:
                pygame.draw.circle(screen, (30, 30, 30), point, 6)

        display_image = player_image_original


        if not facing_right:
            display_image = pygame.transform.flip(display_image, True, False)

        bob_offset = 0
        if is_moving:
            bob_offset = math.sin(walk_timer * 0.3) * 4

        draw_rect = display_image.get_rect(center=(player_rect.centerx, player_rect.centery + bob_offset))
        screen.blit(display_image, draw_rect)

        if not game_over:
            draw_button(game_back_button, "Back", game_back_button.collidepoint(mouse_pos))
            draw_button(pause_button, "Pause", pause_button.collidepoint(mouse_pos))

            timer_text = font.render(f"{int(time_left)}s", True, (20, 20, 20))
            screen.blit(timer_text, (SCREEN_WIDTH // 2 - 20, 20))

            if paused:
                overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                overlay.set_alpha(150)
                overlay.fill((0, 0, 0))
                screen.blit(overlay, (0, 0))

                paused_text = title_font.render("Paused", True, (255, 255, 255))
                screen.blit(paused_text, paused_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80)))
                draw_button(resume_button, "Resume", resume_button.collidepoint(mouse_pos))

        else:
            msg_text = font.render(final_message, True, (255, 255, 255))
            screen.blit(msg_text, (SCREEN_WIDTH // 2 - msg_text.get_width() // 2, SCREEN_HEIGHT // 2))

            if entering_name:
                prompt_text = font.render("Enter your name and press Enter:", True, (255, 255, 255))
                screen.blit(prompt_text, prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)))

                input_box = pygame.Rect(0, 0, 300, 50)
                input_box.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
                pygame.draw.rect(screen, (255, 255, 255), input_box, border_radius=8)
                pygame.draw.rect(screen, (30, 30, 30), input_box, width=2, border_radius=8)

                name_surface = font.render(player_name_input, True, (30, 30, 30))
                screen.blit(name_surface, (input_box.x + 10, input_box.y + 10))
            else:
                draw_button(play_again_button, "Play Again", play_again_button.collidepoint(mouse_pos))
                draw_button(back_to_menu_button, "Back to Menu", back_to_menu_button.collidepoint(mouse_pos))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()