import json

img = open("image_info_test-dev2017.json")
img_row = json.load(img)
print("Кількість зображень:", len(img_row["images"]))
print("Кількість категорій:", len(img_row["categories"]))

for i in range (0, len(img_row["images"])):
    if img_row["images"][i].get("file_name")=="000000000001.jpg":
        print("Coco_url:",img_row["images"][i].get("coco_url"))

        print("Height:",img_row["images"][i].get("height"))

        print("Width:",img_row["images"][i].get("width"))

        print("id:",img_row["images"][i].get("id"))