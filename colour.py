import os
import re

# === USER SETTINGS ===
source_folder = r"C:\folder\path"
output_folder = r"C:\output_folder\path"

color_map = {
    "#bfe8c1": "#fbb84a",  # Replace accents 
    "#231f20": "#696d2c",  # Replace text 
}

background_color = "#fff1e9" # Replace background
# =======================

# Normalize keys in color map
color_map = {k.lower(): v.lower() for k, v in color_map.items()}

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Regex to find 6-digit hex colors
hex_color_pattern = r"#([0-9a-fA-F]{6})"

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".svg"):
        src_path = os.path.join(source_folder, filename)
        out_path = os.path.join(output_folder, filename)

        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace hex colors
        def replace_color(match):
            original = match.group(0)
            hex_clean = original.lower()
            return color_map.get(hex_clean, original)

        # Actually do the replacement
        content = re.sub(hex_color_pattern, replace_color, content, flags=re.IGNORECASE)

        # Add background rect if requested
        if background_color:
            svg_tag = re.search(r"<svg[^>]*>", content)
            if svg_tag:
                tag = svg_tag.group(0)
                width = re.search(r'width="([^"]+)"', tag)
                height = re.search(r'height="([^"]+)"', tag)
                w = width.group(1) if width else "100%"
                h = height.group(1) if height else "100%"
                bg_rect = f'<rect width="{w}" height="{h}" fill="{background_color}" />\n'
                content = content.replace(tag, tag + "\n" + bg_rect)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Processed: {filename}")

print("🎨 Done! All SVGs updated.")

