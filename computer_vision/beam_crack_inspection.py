"""
Basic computer-vision preprocessing for beam/surface inspection images.
Run: python computer_vision/beam_crack_inspection.py path/to/beam_image.jpg

This is NOT a trained crack detector. It highlights dark/edge-like regions for
visual review only; lighting, texture and image quality can cause false results.
"""
import sys
from pathlib import Path
import cv2

if len(sys.argv) < 2:
    raise SystemExit("Usage: python computer_vision/beam_crack_inspection.py image.jpg")
image_path = Path(sys.argv[1])
image = cv2.imread(str(image_path))
if image is None:
    raise SystemExit(f"Could not open image: {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
denoised = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(denoised, 40, 120)
_, dark_regions = cv2.threshold(denoised, 80, 255, cv2.THRESH_BINARY_INV)

out = Path("outputs/computer_vision")
out.mkdir(parents=True, exist_ok=True)
cv2.imwrite(str(out / "grayscale.png"), gray)
cv2.imwrite(str(out / "edge_map.png"), edges)
cv2.imwrite(str(out / "dark_region_candidates.png"), dark_regions)
overlay = image.copy()
overlay[edges > 0] = (0, 0, 255)
cv2.imwrite(str(out / "edge_overlay.png"), overlay)
print(f"Inspection previews saved to {out.resolve()}")
print("Visual candidates only — not a certified crack/severity diagnosis.")
