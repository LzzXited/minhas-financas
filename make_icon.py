import struct, zlib, sys

N = 1024
BG_TOP = (20, 184, 166)
BG_BOT = (15, 118, 110)
WHITE = (255, 255, 255)
GOLD = (251, 191, 36)

px = [[None] * N for _ in range(N)]
for y in range(N):
    t = y / (N - 1)
    c = tuple(round(BG_TOP[i] * (1 - t) + BG_BOT[i] * t) for i in range(3))
    for x in range(N):
        px[y][x] = c

def rect(x0, y0, x1, y1, col, r=0):
    for y in range(y0, y1):
        for x in range(x0, x1):
            # rounded corners
            if r:
                cx = min(max(x, x0 + r), x1 - r - 1)
                cy = min(max(y, y0 + r), y1 - r - 1)
                if (x - cx) ** 2 + (y - cy) ** 2 > r * r:
                    continue
            px[y][x] = col

def circle(cx, cy, rad, col):
    for y in range(cy - rad, cy + rad + 1):
        for x in range(cx - rad, cx + rad + 1):
            if (x - cx) ** 2 + (y - cy) ** 2 <= rad * rad:
                px[y][x] = col

# rising bars inside the adaptive-icon safe zone (~center 60%)
base = 700
bw = 110
gap = 45
x = 512 - (3 * bw + 2 * gap) // 2
for h in (170, 280, 390):
    rect(x, base - h, x + bw, base, WHITE, r=22)
    x += bw + gap
rect(512 - 230, base + 30, 512 + 230, base + 60, WHITE, r=15)
circle(700, 290, 70, GOLD)

raw = b"".join(b"\x00" + bytes(v for p in row for v in p) for row in px)
def chunk(t, d):
    return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", N, N, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
open(sys.argv[1], "wb").write(png)
