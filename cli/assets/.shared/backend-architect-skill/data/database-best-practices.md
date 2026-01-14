# 🗄️ Nguyên Tắc Thiết Kế Database (Database Design Principles)

Tài liệu này tổng hợp các nguyên tắc cốt lõi để thiết kế cơ sở dữ liệu (Relational Database) đảm bảo hiệu năng (Speed), tối ưu lưu trữ (Storage) và khả năng mở rộng (Scalability) cho các hệ thống từ nhỏ đến lớn.

---

## 1. Nguyên Tắc Tạo Bảng (Table Design)

### 1.1. Naming Convention (Quy tắc đặt tên)
- **Tên bảng**: Sử dụng **snake_case**, số nhiều (Plural). Ví dụ: `users`, `orders`, `order_items`.
- **Tên cột**: Sử dụng **snake_case**. Rõ nghĩa, tránh viết tắt gây hiểu nhầm.
- **Primary Key (PK)**: Luôn đặt là `id`. Tránh `user_id` trong bảng `users` (dư thừa).
- **Foreign Key (FK)**: `<tên_bảng_số_ít>_id`. Ví dụ: `user_id` trong bảng `orders`.

### 1.2. Data Types (Kiểu dữ liệu)
- **Chuẩn hóa kích thước**: Sử dụng kiểu dữ liệu nhỏ nhất có thể đáp ứng nhu cầu.
    - Dùng `SMALLINT`, `INTEGER` thay vì `BIGINT` nếu dữ liệu không quá lớn.
    - Dùng `VARCHAR(n)` thay vì `TEXT` nếu có giới hạn rõ ràng (tăng tốc độ sort/index).
- **Tài chính/Tiền tệ**: **TUYỆT ĐỐI KHÔNG** dùng `FLOAT` hay `DOUBLE`. Bắt buộc dùng `DECIMAL` (hoặc `NUMERIC`) để tránh sai số làm tròn.
- **Ngày giờ**:
    - PostgreSQL: Luôn dùng `TIMESTAMPTZ` (có múi giờ) thay vì `TIMESTAMP`.
    - MySQL: Cân nhắc `DATETIME` hoặc `TIMESTAMP` tùy nhu cầu năm 2038.
- **Boolean**: Dùng `BOOLEAN` (Postgres) hoặc `TINYINT(1)` (MySQL).
- **JSON/JSONB**:
    - Chỉ dùng khi cấu trúc dữ liệu thay đổi thường xuyên hoặc không xác định trước.
    - PostgreSQL: Dùng `JSONB` để có thể đánh index và query nhanh hơn (Data được lưu dạng Binary).

### 1.3. Primary Key & ID Strategy
- **Auto Increment (Integer/BigInt)**:
    - *Ưu điểm*: Tốn ít bộ nhớ (4-8 bytes), insert nhanh (tuần tự), tốt cho B-Tree Index.
    - *Nhược điểm*: Dễ bị đoán (Enumeration Attack), khó merge data từ nhiều DB, lộ quy mô hệ thống.
    - *Khuyên dùng*: Cho các bảng nội bộ, ít public ra ngoài, hoặc hệ thống nhỏ/vừa.
- **UUID (Universally Unique Identifier)**:
    - *Ưu điểm*: Unique toàn cầu, bảo mật (không đoán được ID kế tiếp), dễ dàng sharding/merge DB.
    - *Nhược điểm*: Tốn bộ nhớ (16 bytes), làm phân mảnh index (Fragmentation) gây chậm insert.
    - *Khuyên dùng*: Cho các bảng chính (`users`, `orders`), Distributed Systems, Microservices.
- **TSID / UUID v7**:
    - *Giải pháp lai*: UUID có sắp xếp theo thời gian. Khắc phục vấn đề phân mảnh index của Random UUID.
    - **RECOMMENDED** cho hệ thống lớn năm 2025.

### 1.4. Constraints & Nullability
- **NOT NULL**: Mặc định tất cả các cột nên là `NOT NULL` trừ khi có lý do chính đáng. `NULL` làm phức tạp logic query (phải handle `IS NULL`, `IS NOT NULL`) và indexing.
- **Default Values**: Thiết lập giá trị mặc định ở cấp DB thay vì App để đảm bảo tính nhất quán (ví dụ: `status` mặc định 'pending', `created_at` mặc định `NOW()`).
- **Audit Columns**: Mọi bảng nên có `created_at` và `updated_at`.

---

## 2. Nguyên Tắc Về Quan Hệ (Relationships)

### 2.1. Foreign Keys (Khóa ngoại)
- **Luôn khai báo FK Constraint**: Để đảm bảo Data Integrity (tính toàn vẹn dữ liệu). Tránh mồ côi dữ liệu (Orphan record).
- **Indexing Foreign Keys**: Hầu hết các DB **không** tự động đánh index cho FK.
    - **RULE**: Luôn đánh Index cho cột FK. 99% các query `JOIN` hoặc `WHERE` đều lọc theo FK. Nếu thiếu index, DB sẽ phải Full Table Scan.

### 2.2. Cascade Rules
- Cẩn trọng với `ON DELETE CASCADE`. Nếu xóa 1 user dẫn đến xóa 1 triệu logs liên quan, hệ thống sẽ bị treo (Locking).
- *Khuyên dùng*: `ON DELETE RESTRICT` (chặn xóa nếu còn dữ liệu con) hoặc `ON DELETE SET NULL` (nếu logic cho phép). Xử lý xóa dây chuyền nên làm ở Application (Soft Delete) hoặc Background Job.

### 2.3. Many-to-Many
- Luôn sử dụng bảng trung gian (Junction Table).
- PK của bảng trung gian có thể là Composite Key của 2 FKs `(a_id, b_id)` để đảm bảo tính duy nhất.

---

## 3. Nguyên Tắc Indexing & Performance

### 3.1. Chiến thuật Index
- **Index Selectivity**: Chỉ đánh index cột có độ phân tán dữ liệu cao (High Cardinality). Ví dụ: `email`, `phone`. Không index cột như `gender` (chỉ có 2-3 giá trị) vì DB scan bảng còn nhanh hơn.
- **Composite Index (Index ghép)**:
    - Quan trọng thứ tự: Index `(A, B)` hỗ trợ query `WHERE A=... AND B=...` và `WHERE A=...`, nhưng **KHÔNG** hỗ trợ tốt `WHERE B=...`.
    - Nguyên tắc "Leftmost Prefix".
- **Covering Index**: Thêm các cột cần `SELECT` vào index (dùng `INCLUDE` trong Postgres) để DB lấy dữ liệu ngay từ Index mà không cần phải truy xuất vào bảng gốc (Heap fetch).

### 3.2. Không lạm dụng Index
- Mỗi Index làm chậm thao tác `INSERT`, `UPDATE`, `DELETE` vì phải cập nhật cả cây Index.
- Xóa các Index không sử dụng (Dùng thống kê `pg_stat_user_indexes` để kiểm tra).

---

## 4. Nguyên Tắc Functions & Triggers

### 4.1. Stored Functions/Procedures
- **Business Logic belongs to Application Code**: Hạn chế viết logic nghiệp vụ phức tạp trong DB Function. Khó debug, khó version control, khó scale, khó unit test.
- *Ngoại lệ*: Chỉ dùng cho logic liên quan chặt chẽ đến tính toàn vẹn dữ liệu hoặc performance cực cao (batch processing dữ liệu lớn tại chỗ).

### 4.2. Triggers
- **Avoid Triggers if possible**: Trigger ẩn logic, làm cho việc debug trở thành cơn ác mộng ("Tại sao insert bảng A mà bảng B lại đổi??").
- Trigger làm tăng độ trễ (Latency) của transaction.
- *Use Case hợp lý*:
    - Tự động cập nhật `updated_at`.
    - Ghi log audit trail (nếu không dùng thư viện App).
    - Tính toán Denormalization đơn giản (vd: count comment trong bài viết) - nhưng cần cẩn thận deadlocks.

---

## 5. Nguyên Tắc Truy Vấn (Queries)

### 5.1. SELECT
- **NEVER `SELECT *`**: Luôn chỉ định rõ cột cần lấy. `SELECT *` gây lãng phí băng thông mạng, RAM, và ngăn cản Covering Index.
- **N+1 Problem**: Là lỗi phổ biến nhất giết chết performance.
    - *Triệu chứng*: Select list users (1 query), sau đó loop qua user để select address (N queries).
    - *Giải pháp*: Dùng `JOIN` hoặc `WHERE IN` (Eager Loading trong ORM).

### 5.2. Filtering & Sorting
- Đảm bảo cột trong `WHERE`, `JOIN`, `ORDER BY` đã được đánh Index.
- Tránh tính toán trên cột trong `WHERE`:
    - *Bad*: `WHERE YEAR(created_at) = 2024` (Không dùng được Index).
    - *Good*: `WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'`.

### 5.3. Phân trang (Pagination)
- **OFFSET / LIMIT**: Chậm khi số trang lớn (DB phải scan và bỏ qua N dòng đầu).
- **Keyset Pagination (Cursor-based)**: Dùng `WHERE id > last_seen_id LIMIT 20`. Siêu nhanh bất kể dữ liệu lớn cỡ nào.

---

## 6. Tối Ưu Lưu Trữ & Scale (Storage & Optimization)

### 6.1. Partitioning (Phân mảnh bảng)
- Khi bảng > 10 triệu dòng (hoặc 100GB+), cân nhắc Partitioning.
- Phổ biến nhất: Partition theo Time (Logs tháng 1, Logs tháng 2...). Giúp query nhanh (Pruning) và dễ dàng Archive/Delete dữ liệu cũ (Drop Partition cực nhanh so với Delete từng dòng).

### 6.2. Denormalization (Phi chuẩn hóa)
- Chỉ thực hiện khi đã optimize hết mức mà vẫn chậm (Read-heavy).
- Ví dụ: Lưu `total_orders` vào bảng `users` để khỏi `COUNT(*)` mỗi lần query. Chấp nhận rủi ro dữ liệu lệch (cần cơ chế đồng bộ lại).

### 6.3. Connection Pooling
- DB connection (đặc biệt Postgres) rất đắt đỏ (process-based).
- HỆ THỐNG PHẢI DÙNG Connection Pooler (như PgBouncer hoặc library pooler HikariCP/Go-sql-driver). Không bao giờ mở new connection cho mỗi request.
