import os

# 配置
username = "VerspotTechnology"
repo = "Diamond-Treasure"
branch = "main"
folder = "images"  # 要扫描的文件夹

base_url = f"https://cdn.jsdelivr.net/gh/{username}/{repo}@{branch}/"

links = []

for root, dirs, files in os.walk(folder):
    for file in files:
        rel_path = os.path.relpath(os.path.join(root, file), ".")
        cdn_url = base_url + rel_path.replace("\\", "/")
        links.append(cdn_url)

# 输出到文件
with open("cdn_links.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(links))

print("✅ 已生成 cdn_links.txt，里面包含所有图片的 jsDelivr 链接")
