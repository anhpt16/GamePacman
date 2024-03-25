Chương 2: Xây dựng chương trình
2.1. Mô tả trò chơi
Pacman là một trò chơi kinh điển trở thành biểu tượng của văn hóa đại chúng từ những năm 80. Trong trò chơi người chơi sẽ điều khiển Pacman trong một mê cung và ăn các chấm pac. Nếu người chơi ăn hết chấm pac thì sẽ được qua màn. Có 4 đối thủ là Blinky, Pinky, Inky và Clyde đi tự do trong mê cung và sẽ cố gắng để bắt Pacman. Nếu bị bắt Pacman sẽ bị mất mạng. Trong mê cung có các chấm tròn to (big pac) hay còn gọi là viên sức mạnh, khi ăn được các chấm này Pacman sẽ có khả năng ăn kẻ địch trong một khoảng thời gian ngắn. Khi đó kẻ địch sẽ chuyển sang màu lam, di chuyển chậm lại và chạy trốn khỏi Pacman. Khi một kẻ địch bị ăn, đôi mắt của chúng sẽ di chuyển về vị trí hồi sinh ở trung tâm màn hình, sau đó chung sẽ được hồi sinh lại như ban đầu.
	Pacman: người chơi sẽ sử dụng cái phím mũi tên để giúp pacman chuyển hướng trong mê cung, giúp pacman tránh khỏi sự truy đuổi của 4 con ma và ăn hết các chấm pac. Mỗi khi bị giết bởi các con ma, Pacman sẽ bị trừ đi một mạng và khi không còn mạng nào trò chơi sẽ kết thúc.
	Ghosts: 4 con ma sẽ có các trạng thái: đuổi bắt pacman, ngừng đuổi bắt và chạy khỏi pacman – khi panman ăn được viên sức mạnh. Khi bị pacman giết, nó sẽ chuyển thành hình đôi mắt và di chuyển về nơi hồi sinh và sẽ được hồi sinh sau một khoảng thời gian sau đó lại tiếp tục đuổi bắt pacman. Mỗi con ma sẽ được cài đặt các cách di chuyển khác nhau. 
2.2. Các bước xây dựng trò chơi.
Nhóm đã thực hiện các bước sau để xây dựng trò chơi
+	Bước 1: Tạo mê cung và các chấm pac.
+	Bước 2: Tạo pacman bao gồm các thuộc tính và chuyển động cho pacman.
+	Bước 3: Tạo ra các ghost bao gồm các thuộc tính cho ghost và cách di chuyển của ghost.
Bước 1: Tạo mê cung và các chấm pac
Sử dụng một mảng 2 chiều có kích thước 30x32 để tạo mê cung. Trong đó:
+	Giá trị 0: là các khoảng trống màu đen trong mê cung;
+	Giá trị 1: là các chấm pac;
+	Giá trị 2: là các chấm big – pac;
+	Giá trị 3,4,5,6,7,8: lần lượt là các giá trị đại diện cho các cạnh của bức tường;
+	Giá trị 9: là các cánh cổng hồi sinh;
![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/a530059b-bddb-4228-8c3f-f0ad308b2a98)

![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/c8fa1b01-942f-44e5-9234-75f5941214fc)

Bước 2: Tạo Pacman, các thuộc tính và chuyển động cho Pacman.
Tạo Pacman:
-	Pacman sẽ có các hình ảnh khác nhau khi người chơi chuyển hướng pacman trong mê cung;
-	Các hình ảnh đó tương ứng với các dirrection 0, 1,  2 và 3.
-	
![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/45253bee-600b-481d-b02d-c91f8ed38f22)

![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/d97fd75e-ada8-4db6-8bd0-a612bb068e8e)

 
Kiểm tra vị trí di chuyển của Pacman:
-	Pacman chỉ được phép chuyển hướng hoặc quay lại ở các ô có giá trị cho phép (0, 1 và 2);
-	Do đó, mỗi lần di chuyển các vị trí mà pacman đang hướng đến luôn phải được kiểm tra trước xem vị trí đó có thể đi hay không để pacman có thể tránh đi vào các bức tường.
-	
![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/a57ac0e4-2497-4437-b27e-d1e7d807ac88)

Tạo chuyển động cho Pacman:
-	Để chuyển hướng Pacman trong mê cung, người chơi sử dụng phím mũi tên và trước khi chuyển hướng đến mũi tên được nhấn, vị trí của nó sẽ được kiểm tra.
-	
![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/e382b4eb-161d-4a7a-adc2-9ff5f29c843a)


Bước 3: Tạo các Ghost, các thuộc tính và cách di chuyển cho các Ghost
Tạo ghost và tọa độ mặc định của ghost trên map:
-	Thao tác tạo ghost tương tự với Pacman nhưng ghost chỉ cần 1 ảnh để hiển thị trong suốt quá trình chuyển hướng.
-	
![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/e0e935b7-c4d7-4482-94aa-8d561e94211e)

-	Thiết lập tọa độ mặc định cho ghost
-	
![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/62f32b9a-47ab-41f9-b1ec-7791df8fb313)

![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/94eb6b9b-e0cc-4032-8279-525feb356052)

 
Tạo cách di chuyển cho các ghost:
-	Ghost sẽ di chuyển theo đường dẫn được lựa chọn trong hàm check_path_ghost;
-	Các câu lệnh điều kiện kiểm tra quãng đường đi được và điều hướng cho ghost khi cần.
-	
![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/64e74de5-954f-4a5b-a900-c90b62927598)
 

2.3. Áp dụng thuật toán A* vào trò chơi
2.3.1. Ý tưởng xây dựng thuật toán: 
Mỗi một ô trên map có các giá trị là 0, 1 và 2 đều có thể di chuyển được. Do đó, ta thiết lập các ô này làm các node. Vì ghost và Pacman luôn luôn di chuyển trên các node do đó ghost có thể dễ dàng tìm thấy được Pacman khi nó di chuyển. 
Một thuật giải A* cơ bản cần có các chỉ số: nút xét, các nút kề với nút đang xét, danh sách mở lưu trữ các các nút cho các lần xét tiếp theo và danh sách đóng lưu trữ các nút đã được xét. Ngoài ra, thuật giả A* còn sử dụng hàm f = g + h để đánh giá các nút. Trong đó, g là chi phí đường đi từ nút ban đầu cho tới nút đang xét còn f là chi phí ước lượng tính từ nút đang xét tới nút đích.
Để áp dụng thuật giải này vào trong trò chơi, ta sử dụng khoảng cách Manhattan cho hàm ước lượng h, đây là một dạng khoảng cách giữa hai điểm trong không gian Euclid với hệ tọa độ Descartes. Đại lượng này được tính bằng tổng chiều dài của hình chiếu đường của đường thẳng nối hai điểm này trong hệ trục tọa độ Descartes. Khoảng cách Manhattan giữa hai điểm P1(x1, y1) và P2(x2, y2) là: 
|x1 – x2| + |y1 – y2|
Ngoài sử dụng khoảng cách Manhattan cho hàm heuristic h ta còn có thể sử dụng khoảng cách chéo hay khoảng cách Euclide cho hàm này. Nhưng trong trò chơi này nhóm em sử dụng khoảng cách Manhattan cho hàm h vì hàm này sẽ tối ưu nhất cho những bài toán chỉ được phép di chuyển theo 4 hướng (trái, phải, trên, dưới).
2.3.2. Áp dụng thuật toán
	Các bước triển khai theo thứ tự trong thuật toán A* đó là: Từ nút bắt đầu, đưa ra các nút kề với nút đầu, đưa các nút kề vào một danh sách, đưa nút đang xét vào danh sách đóng ,xem xét và tìm ra nút tối ưu trong danh sách, xét nút tối ưu, đưa ra các nút kề với nút tối ưu, đưa các nút kề vào danh sách, đưa nút đang xét vào danh sách đóng, chọn nút tối ưu trong danh sách, ... Quá trình này tiếp tục cho đến khi nút tối ưu được tìm thấy là nút kết thúc.
	Bước đầu tiên cần phải làm trong thuật toán này đó là: tìm ra các nút kề với nút đang xét (hay đưa ra các node kề với node đang xét). Để thực hiện điều này ta tạo một hàm xem xét các nút, hàm này được đặt tên là: check_ghost_node_plus. Với các tham số đầu vào của hàm là: vị trí hàng hiện tại, vị trí cột hiện tại, vị trí hàng đích, vị trí cột đích, chi phí tại vị trí hiện tại tương ứng với các tham số lần lượt là (pos_x, pos_y, pac_x, pac_y, g0). Giá trị trả về của hàm là danh sách các node kề với node hiện tại:
 
  ![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/32257f14-8466-4464-ab87-859fe81369fd)

	Trong hàm này, ta lần lượt kiểm tra 4 vị trí xung quanh node hiện tại để phát hiện các node kề (các node có giá trị 0, 1 và 2). Ngoài ra, các giá trị g, h, f tại nút đó cũng được tính toán theo. Cuối cùng các node được thêm vào list_node đã được khai báo ban đầu và trả về khi hoàn thành xong hàm này. Mỗi một chỉ số trong list_node sẽ lưu trữ các giá trị (vị trí hàng hiện tại, vị trí cột hiện tại, g, h, f, vị trí hàng của nút cha, vị trí cột của nút cha).
	Bước 2 sau khi đã có các node kề, ta phải lựa chọn các các node cho đến khi nào node được chọn là node đích và lúc đó ta sẽ tìm được đường đi. Vậy nên ta sẽ tạo một hàm đảm nhiệm nhiệm vụ tìm đường dẫn từ node hiện tại tới node đích. Hàm này sẽ có tên là: check_path_ghost. Đầu vào của hàm bao gồm vị trí hàng hiện tại, vị trí cột hiện tại, vị trí hàng đích, vị trí cột đích tương ứng với các tham số lần lượt là (ghost_x, ghost_y, pac_x, pac_y). Tạo các giá trị g, h, f cho nút xét và đưa nó vào danh sách mở. Sau đó là lần lượt các thao tác đưa các node vào tập mở lấy các node ra khỏi tập mở, thêm các node vao tập đóng cho đến khi tìm được node đích, chúng ta thêm node đích vào tập đóng và thoát khỏi vòng lặp while.
	Lúc này tập đóng sẽ chứa các node đường dẫn từ node đầu cho đến node đích. Chúng ta sử dụng một danh sách nữa có tên là best_path để lưu trữ và truy ngược đường dẫn. Lúc này giá trị trả về của hàm check_path_ghost này là best_path có lưu trữ đường dẫn tối ưu từ node đầu cho tới node cuối.
 
  ![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/e9a1c0c5-454a-4220-887c-82a5c9f53785)
  
  ![ảnh](https://github.com/anhpt16/GamePacman/assets/132929711/61470576-6399-4596-8f6d-56ead6976f2d)
  
  Bước cuối cùng là sử dụng hàm move_ghost đã được giới thiệu phía trên để đưa ghost đi theo đường dẫn đã tìm được. Đầu vào của hàm nào bao gồm các giá trị (tọa độ trục hoành của ghost, tọa độ trục tung của ghost, tọa độ trục hoành của pacman, tọa độ trục tung của pacman). Đầu ra của hàm là trả về các giá trị đã cập nhật cho vị trí của ghost và vị trí của pacman. Hàm này sẽ đảm nhiệm vai trò chuyển đổi các vị trí tung độ, hoành độ của ghost và pacman thành các chỉ số hàng và cột để thuận tiện cho việc tính toán.
