import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Thiết lập font cho tiếng Việt (nếu có)
plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'sans-serif']

def ve_so_do_luong_chuong_trinh():
    """Vẽ sơ đồ lưồng chương trình đơn giản"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Các hình chữ nhật và hình oval
    boxes = [
        {'type': 'oval', 'pos': (5, 9), 'size': (2, 0.8), 'text': 'Bắt đầu', 'color': 'lightgreen'},
        {'type': 'rect', 'pos': (4, 7.5), 'size': (4, 1), 'text': 'Nhập dữ liệu', 'color': 'lightblue'},
        {'type': 'diamond', 'pos': (5, 6), 'size': (3, 1.2), 'text': 'Kiểm tra\nđiều kiện?', 'color': 'yellow'},
        {'type': 'rect', 'pos': (2, 4), 'size': (3, 1), 'text': 'Xử lý A', 'color': 'lightcoral'},
        {'type': 'rect', 'pos': (7, 4), 'size': (3, 1), 'text': 'Xử lý B', 'color': 'lightcoral'},
        {'type': 'rect', 'pos': (4, 2), 'size': (4, 1), 'text': 'Xuất kết quả', 'color': 'lightblue'},
        {'type': 'oval', 'pos': (5, 0.5), 'size': (2, 0.8), 'text': 'Kết thúc', 'color': 'lightgreen'}
    ]
    
    # Vẽ các hình
    for box in boxes:
        x, y = box['pos']
        w, h = box['size']
        
        if box['type'] == 'rect':
            rect = patches.Rectangle((x-w/2, y-h/2), w, h, 
                                   linewidth=2, edgecolor='black', 
                                   facecolor=box['color'])
            ax.add_patch(rect)
        elif box['type'] == 'oval':
            ellipse = patches.Ellipse((x, y), w, h, 
                                    linewidth=2, edgecolor='black', 
                                    facecolor=box['color'])
            ax.add_patch(ellipse)
        elif box['type'] == 'diamond':
            diamond = patches.Polygon([(x, y+h/2), (x+w/2, y), (x, y-h/2), (x-w/2, y)],
                                    linewidth=2, edgecolor='black', 
                                    facecolor=box['color'])
            ax.add_patch(diamond)
        
        # Thêm text
        ax.text(x, y, box['text'], ha='center', va='center', 
                fontsize=10, weight='bold')
    
    # Vẽ các mũi tên
    arrows = [
        ((5, 8.6), (5, 8.0)),  # Bắt đầu -> Nhập dữ liệu
        ((5, 7.0), (5, 6.6)),  # Nhập dữ liệu -> Kiểm tra
        ((4.2, 5.4), (3.5, 4.5)),  # Kiểm tra -> Xử lý A
        ((5.8, 5.4), (7.5, 4.5)),  # Kiểm tra -> Xử lý B
        ((3.5, 3.5), (5, 2.5)),  # Xử lý A -> Xuất kết quả
        ((7.5, 3.5), (6, 2.5)),  # Xử lý B -> Xuất kết quả
        ((5, 1.5), (5, 0.9))   # Xuất kết quả -> Kết thúc
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    # Thêm label cho điều kiện
    ax.text(3.2, 5.2, 'Đúng', ha='center', va='center', fontsize=9, color='red')
    ax.text(6.8, 5.2, 'Sai', ha='center', va='center', fontsize=9, color='red')
    
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Sơ đồ lưồng chương trình', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def ve_so_do_to_chuc():
    """Vẽ sơ đồ tổ chức đơn giản"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Định nghĩa các vị trí và thông tin
    positions = {
        'CEO': (6, 7),
        'Manager1': (3, 5),
        'Manager2': (9, 5),
        'Employee1': (1.5, 3),
        'Employee2': (4.5, 3),
        'Employee3': (7.5, 3),
        'Employee4': (10.5, 3)
    }
    
    labels = {
        'CEO': 'Giám đốc',
        'Manager1': 'Trưởng phòng A',
        'Manager2': 'Trưởng phòng B',
        'Employee1': 'Nhân viên 1',
        'Employee2': 'Nhân viên 2',
        'Employee3': 'Nhân viên 3',
        'Employee4': 'Nhân viên 4'
    }
    
    # Vẽ các hộp
    for pos_key, (x, y) in positions.items():
        if 'CEO' in pos_key:
            color = 'gold'
            size = (2.5, 1)
        elif 'Manager' in pos_key:
            color = 'lightblue'
            size = (2.2, 0.8)
        else:
            color = 'lightgreen'
            size = (2, 0.7)
        
        rect = patches.Rectangle((x-size[0]/2, y-size[1]/2), size[0], size[1],
                               linewidth=2, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(x, y, labels[pos_key], ha='center', va='center', 
                fontsize=10, weight='bold')
    
    # Vẽ các đường kết nối
    connections = [
        ('CEO', 'Manager1'),
        ('CEO', 'Manager2'),
        ('Manager1', 'Employee1'),
        ('Manager1', 'Employee2'),
        ('Manager2', 'Employee3'),
        ('Manager2', 'Employee4')
    ]
    
    for start, end in connections:
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        ax.plot([x1, x2], [y1-0.5, y2+0.4], 'k-', linewidth=2)
    
    ax.set_xlim(-1, 13)
    ax.set_ylim(1, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Sơ đồ tổ chức công ty', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def ve_bieu_do_cot():
    """Vẽ biểu đồ cột đơn giản"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Dữ liệu mẫu
    categories = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6']
    values = [23, 45, 56, 78, 32, 67]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0']
    
    bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)
    
    # Thêm giá trị trên đầu mỗi cột
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{value}', ha='center', va='bottom', fontweight='bold')
    
    ax.set_xlabel('Tháng', fontsize=12, weight='bold')
    ax.set_ylabel('Doanh số (triệu VNĐ)', fontsize=12, weight='bold')
    ax.set_title('Biểu đồ doanh số theo tháng', fontsize=14, weight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def ve_bieu_do_tron():
    """Vẽ biểu đồ tròn đơn giản"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    # Dữ liệu mẫu
    labels = ['Sản phẩm A', 'Sản phẩm B', 'Sản phẩm C', 'Sản phẩm D', 'Khác']
    sizes = [30, 25, 20, 15, 10]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    explode = (0.1, 0, 0, 0, 0)  # Tách phần đầu tiên
    
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, 
                                     colors=colors, autopct='%1.1f%%',
                                     shadow=True, startangle=90)
    
    # Làm đẹp text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('Phân bổ doanh số theo sản phẩm', fontsize=14, weight='bold')
    
    plt.tight_layout()
    return fig

def main():
    """Hàm chính để chạy tất cả các ví dụ"""
    print("Đang tạo các sơ đồ...")
    
    # Tạo và hiển thị sơ đồ lưồng
    fig1 = ve_so_do_luong_chuong_trinh()
    plt.figure(fig1.number)
    plt.show()
    
    # Tạo và hiển thị sơ đồ tổ chức
    fig2 = ve_so_do_to_chuc()
    plt.figure(fig2.number)
    plt.show()
    
    # Tạo và hiển thị biểu đồ cột
    fig3 = ve_bieu_do_cot()
    plt.figure(fig3.number)
    plt.show()
    
    # Tạo và hiển thị biểu đồ tròn
    fig4 = ve_bieu_do_tron()
    plt.figure(fig4.number)
    plt.show()
    
    print("Hoàn thành! Tất cả sơ đồ đã được tạo.")

if __name__ == "__main__":
    main()