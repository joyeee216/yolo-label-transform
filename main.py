import os

# 类别映射字典
category_map = {
   '0':1,
   '1':2,
   '2':0,
    '3':5

}


# 修改文件夹中的标注
def update_annotation_file(file_path, category_map):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        # 每一行的格式是: <class_id> <x_center> <y_center> <width> <height>
        parts = line.strip().split()
        class_name = parts[0]  # 假设类别名在第一列
        # 根据类别映射更新 class_id
        new_class_id = category_map.get(class_name)
        if new_class_id is not None:
            parts[0] = str(new_class_id)
            updated_lines.append(" ".join(parts))
        else:
            print(f"未知类别: {class_name}, 跳过该行")

    # 保存更新后的文件
    with open(file_path, 'w') as file:
        file.write("\n".join(updated_lines))


# 文件夹路径
folders = ['labeldata1-200']

# 遍历文件夹中的所有标注文件并更新
for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder, filename)
            update_annotation_file(file_path, category_map)

print("标注文件更新完毕！")
