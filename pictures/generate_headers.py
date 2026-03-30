#!/usr/bin/env python3
"""Generate header images for the vibe coding playbook."""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
WIDTH = 1200
HEIGHT = 400
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Color palette - modern dark theme with accent colors
COLORS = {
    "bg": (20, 20, 30),  # Dark navy
    "accent1": (100, 200, 255),  # Cyan
    "accent2": (255, 100, 150),  # Pink
    "accent3": (100, 255, 180),  # Mint
    "accent4": (255, 200, 100),  # Gold
    "text": (255, 255, 255),  # White
    "subtle": (60, 60, 80),  # Subtle gray
}


def load_font(size):
    """Try to load a nice font, fall back to default."""
    try:
        # Try common font paths
        for path in [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]:
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    except:
        pass
    return ImageFont.load_default()


def create_gradient_bg(draw, width, height):
    """Create a subtle gradient background."""
    for y in range(height):
        # Simple vertical gradient
        ratio = y / height
        r = int(COLORS["bg"][0] + (COLORS["subtle"][0] - COLORS["bg"][0]) * ratio)
        g = int(COLORS["bg"][1] + (COLORS["subtle"][1] - COLORS["bg"][1]) * ratio)
        b = int(COLORS["bg"][2] + (COLORS["subtle"][2] - COLORS["bg"][2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))


def draw_decorative_circles(draw, width, height):
    """Draw abstract decorative circles."""
    # Large circle top right
    draw.ellipse(
        [width - 300, -100, width + 100, 200], fill=COLORS["accent1"][:3] + (30,)
    )
    draw.ellipse(
        [width - 250, -50, width + 50, 150], fill=COLORS["accent1"][:3] + (50,)
    )

    # Medium circle bottom left
    draw.ellipse(
        [-150, height - 200, 150, height + 50], fill=COLORS["accent2"][:3] + (30,)
    )
    draw.ellipse([-100, height - 150, 100, height], fill=COLORS["accent2"][:3] + (50,))

    # Small accent dots
    draw.ellipse(
        [width // 3, height - 50, width // 3 + 20, height - 30],
        fill=COLORS["accent3"][:3],
    )
    draw.ellipse(
        [width * 2 // 3, 50, width * 2 // 3 + 15, 65], fill=COLORS["accent4"][:3]
    )


def generate_readme_header():
    """Main header for README."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    # Title
    font_title = load_font(72)
    font_subtitle = load_font(32)

    title = "Vibe Coding"
    subtitle = "Playbook"

    # Calculate text position
    bbox_title = draw.textbbox((0, 0), title, font=font_title)
    w_title = bbox_title[2] - bbox_title[0]

    bbox_sub = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    w_sub = bbox_sub[2] - bbox_sub[0]

    draw.text(
        ((WIDTH - w_title) // 2, HEIGHT // 2 - 40),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w_sub) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent1"],
    )

    img.save(f"{OUTPUT_DIR}/README.png")


def generate_git_header():
    """Header for Git & GitHub section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Git & GitHub"
    subtitle = "Version control for vibe coders"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent1"],
    )

    # Draw git branch icon representation
    draw.ellipse(
        [80, HEIGHT // 2 - 60, 130, HEIGHT // 2 - 10],
        outline=COLORS["accent3"],
        width=3,
    )
    draw.line(
        [105, HEIGHT // 2 - 60, 105, HEIGHT // 2 + 60], fill=COLORS["accent3"], width=3
    )
    draw.ellipse(
        [80, HEIGHT // 2 + 30, 130, HEIGHT // 2 + 80],
        outline=COLORS["accent3"],
        width=3,
    )

    img.save(f"{OUTPUT_DIR}/01-git-github.png")


def generate_context_header():
    """Header for Context Files section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Context Files"
    subtitle = "Briefing your AI before you start"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent2"],
    )

    # Draw document stack icon
    for i, offset in enumerate([0, 20, 40]):
        draw.rectangle(
            [
                100 + offset,
                HEIGHT // 2 - 40 + offset,
                200 + offset,
                HEIGHT // 2 + 40 + offset,
            ],
            outline=COLORS["accent1"],
            width=2,
        )

    img.save(f"{OUTPUT_DIR}/02-context-files.png")


def generate_practices_header():
    """Header for Best Practices section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Best Practices"
    subtitle = "Slash commands, agents & MCP"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent3"],
    )

    # Draw gear/cog icon
    center_x, center_y = 150, HEIGHT // 2
    draw.ellipse(
        [center_x - 30, center_y - 30, center_x + 30, center_y + 30],
        outline=COLORS["accent4"],
        width=3,
    )
    draw.ellipse(
        [center_x - 15, center_y - 15, center_x + 15, center_y + 15], fill=COLORS["bg"]
    )

    img.save(f"{OUTPUT_DIR}/03-best-practices.png")


def generate_workflow_header():
    """Header for Workflow section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Workflow"
    subtitle = "The per-session loop"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent4"],
    )

    # Draw cycle arrows
    cx, cy = 150, HEIGHT // 2
    draw.ellipse(
        [cx - 40, cy - 40, cx + 40, cy + 40], outline=COLORS["accent1"], width=3
    )

    img.save(f"{OUTPUT_DIR}/04-workflow.png")


def generate_tools_header():
    """Header for OpenCode vs Claude Code section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(48)
    font_subtitle = load_font(28)

    title = "OpenCode vs Claude Code"
    subtitle = "Tool comparison & specifics"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent1"],
    )

    # Draw two columns representation
    draw.rectangle(
        [80, HEIGHT // 2 - 60, 200, HEIGHT // 2 + 60],
        outline=COLORS["accent2"],
        width=2,
    )
    draw.rectangle(
        [WIDTH - 200, HEIGHT // 2 - 60, WIDTH - 80, HEIGHT // 2 + 60],
        outline=COLORS["accent3"],
        width=2,
    )

    img.save(f"{OUTPUT_DIR}/05-opencode-vs-claude-code.png")


def generate_resources_header():
    """Header for Resources section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Resources"
    subtitle = "Stay current with the tools"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent1"],
    )

    # Draw link chain icon
    center_x, center_y = 150, HEIGHT // 2
    draw.ellipse(
        [center_x - 20, center_y - 20, center_x + 20, center_y + 20],
        outline=COLORS["accent3"],
        width=3,
    )
    draw.ellipse(
        [center_x + 10, center_y - 20, center_x + 50, center_y + 20],
        outline=COLORS["accent3"],
        width=3,
    )

    img.save(f"{OUTPUT_DIR}/06-resources.png")


def generate_whatis_header():
    """Header for What is Vibe Coding section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "What is Vibe Coding?"
    subtitle = "The mental model"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent2"],
    )

    # Draw brain/architecture icon
    center_x, center_y = 150, HEIGHT // 2
    # Brain outline
    draw.ellipse(
        [center_x - 40, center_y - 30, center_x + 40, center_y + 30],
        outline=COLORS["accent1"],
        width=3,
    )
    # Left lobe
    draw.ellipse(
        [center_x - 30, center_y - 20, center_x - 10, center_y + 10],
        fill=COLORS["accent1"],
    )
    # Right lobe
    draw.ellipse(
        [center_x + 10, center_y - 20, center_x + 30, center_y + 10],
        fill=COLORS["accent1"],
    )
    # Brain stem
    draw.rectangle(
        [center_x - 5, center_y + 30, center_x + 5, center_y + 50],
        fill=COLORS["accent1"],
    )

    img.save(f"{OUTPUT_DIR}/00-what-is-vibe-coding.png")


def generate_prompt_engineering_header():
    """Header for Prompt Engineering section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Prompt Engineering"
    subtitle = "Write prompts that get results"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent2"],
    )

    # Draw chat bubble icon
    cx, cy = 150, HEIGHT // 2
    draw.rounded_rectangle(
        [cx - 40, cy - 30, cx + 40, cy + 15],
        radius=10,
        outline=COLORS["accent2"],
        width=3,
    )
    draw.polygon(
        [cx - 10, cy + 15, cx - 25, cy + 35, cx + 5, cy + 15],
        fill=COLORS["accent2"],
    )

    img.save(f"{OUTPUT_DIR}/07-prompt-engineering.png")


def generate_debugging_header():
    """Header for Debugging with Agents section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Debugging with Agents"
    subtitle = "Fix bugs with AI help"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent4"],
    )

    # Draw bug icon
    cx, cy = 150, HEIGHT // 2
    draw.ellipse(
        [cx - 25, cy - 25, cx + 25, cy + 25],
        outline=COLORS["accent4"],
        width=3,
    )
    # Antennae
    draw.line([cx - 10, cy - 25, cx - 20, cy - 45], fill=COLORS["accent4"], width=3)
    draw.line([cx + 10, cy - 25, cx + 20, cy - 45], fill=COLORS["accent4"], width=3)
    # Legs
    draw.line([cx - 25, cy - 10, cx - 40, cy - 15], fill=COLORS["accent4"], width=2)
    draw.line([cx - 25, cy + 10, cx - 40, cy + 15], fill=COLORS["accent4"], width=2)
    draw.line([cx + 25, cy - 10, cx + 40, cy - 15], fill=COLORS["accent4"], width=2)
    draw.line([cx + 25, cy + 10, cx + 40, cy + 15], fill=COLORS["accent4"], width=2)

    img.save(f"{OUTPUT_DIR}/08-debugging-with-agents.png")


def generate_project_types_header():
    """Header for Project Types section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Project Types"
    subtitle = "Start the right way"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent3"],
    )

    # Draw stacked blocks icon
    for i, offset in enumerate([0, 30, 60]):
        draw.rectangle(
            [110 + offset, HEIGHT // 2 - 40, 180 + offset, HEIGHT // 2 + 40],
            outline=COLORS["accent3"],
            width=2,
        )

    img.save(f"{OUTPUT_DIR}/09-project-types.png")


def generate_cost_models_header():
    """Header for Cost and Models section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Cost and Models"
    subtitle = "Manage API costs"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent1"],
    )

    # Draw dollar sign icon
    cx, cy = 150, HEIGHT // 2
    font_icon = load_font(60)
    draw.text((cx - 15, cy - 35), "$", font=font_icon, fill=COLORS["accent1"])

    img.save(f"{OUTPUT_DIR}/10-cost-and-models.png")


def generate_session_management_header():
    """Header for Managing Sessions section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Managing Sessions"
    subtitle = "Resume, fork, and revert"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent2"],
    )

    # Draw branching/fork icon
    cx, cy = 150, HEIGHT // 2
    draw.line([cx - 40, cy, cx, cy], fill=COLORS["accent2"], width=3)
    draw.line([cx, cy, cx + 30, cy - 30], fill=COLORS["accent2"], width=3)
    draw.line([cx, cy, cx + 30, cy + 30], fill=COLORS["accent2"], width=3)
    # Dots at branch points
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=COLORS["accent2"])
    draw.ellipse([cx + 22, cy - 38, cx + 38, cy - 22], fill=COLORS["accent2"])
    draw.ellipse([cx + 22, cy + 22, cx + 38, cy + 38], fill=COLORS["accent2"])

    img.save(f"{OUTPUT_DIR}/11-session-management.png")


def generate_roadmap_header():
    """Header for Roadmap section."""
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["bg"])
    draw = ImageDraw.Draw(img)

    create_gradient_bg(draw, WIDTH, HEIGHT)
    draw_decorative_circles(draw, WIDTH, HEIGHT)

    font_title = load_font(56)
    font_subtitle = load_font(28)

    title = "Roadmap"
    subtitle = "Future expansions"

    bbox = draw.textbbox((0, 0), title, font=font_title)
    w = bbox[2] - bbox[0]

    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 - 30),
        title,
        font=font_title,
        fill=COLORS["text"],
    )
    draw.text(
        ((WIDTH - w) // 2, HEIGHT // 2 + 40),
        subtitle,
        font=font_subtitle,
        fill=COLORS["accent3"],
    )

    # Draw road/map icon
    cx, cy = 150, HEIGHT // 2
    # Road
    draw.rectangle([cx - 50, cy + 20, cx + 50, cy + 40], fill=COLORS["subtle"])
    # Lane markings
    for i in range(-40, 41, 20):
        draw.rectangle([cx + i - 2, cy + 25, cx + i + 2, cy + 35], fill=COLORS["text"])
    # Map pin
    draw.ellipse([cx - 10, cy - 30, cx + 10, cy - 10], fill=COLORS["accent3"])
    draw.line([cx, cy - 30, cx, cy - 50], fill=COLORS["accent3"], width=3)
    draw.ellipse([cx - 4, cy - 54, cx + 4, cy - 46], fill=COLORS["accent3"])

    img.save(f"{OUTPUT_DIR}/12-roadmap.png")


if __name__ == "__main__":
    print("Generating section header images...")
    print("(Skipping README.png — do not modify)\n")

    generate_whatis_header()
    print("✓ 00-what-is-vibe-coding.png")

    generate_git_header()
    print("✓ 01-git-github.png")

    generate_context_header()
    print("✓ 02-context-files.png")

    generate_practices_header()
    print("✓ 03-best-practices.png")

    generate_workflow_header()
    print("✓ 04-workflow.png")

    generate_tools_header()
    print("✓ 05-opencode-vs-claude-code.png")

    generate_resources_header()
    print("✓ 06-resources.png")

    generate_prompt_engineering_header()
    print("✓ 07-prompt-engineering.png")

    generate_debugging_header()
    print("✓ 08-debugging-with-agents.png")

    generate_project_types_header()
    print("✓ 09-project-types.png")

    generate_cost_models_header()
    print("✓ 10-cost-and-models.png")

    generate_session_management_header()
    print("✓ 11-session-management.png")

    generate_roadmap_header()
    print("✓ 12-roadmap.png")

    print(f"\nAll images saved to {OUTPUT_DIR}/")
