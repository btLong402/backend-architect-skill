# Danh sách Kiểm tra Bảo mật Backend (Phiên bản 2025-2026)

Danh sách này thực thi các giao thức bảo mật bắt buộc cho hệ thống backend, tuân thủ các tiêu chuẩn OWASP Top 10 2025, NIST SP 800-63B, và SLSA Level 3.

## 1. Xác thực & Định danh (NIST & OAuth 2.1)
- [ ] **Chính sách Mật khẩu**:
    - [ ] Độ dài tối thiểu: **15 ký tự** cho đơn yếu tố (single-factor), 8 ký tự cho đa yếu tố (MFA).
    - [ ] **Không áp dụng quy tắc phức tạp** (loại bỏ yêu cầu bắt buộc ký tự đặc biệt/số).
    - [ ] **Không ép buộc xoay vòng** (hết hạn) trừ khi nghi ngờ bị lộ.
    - [ ] Hỗ trợ độ dài tối đa: ít nhất 64 ký tự.
    - [ ] Sàng lọc thông tin xác thực: Chặn các mật khẩu nằm trong danh sách bị lộ đã biết (ví dụ: HaveIBeenPwned).
- [ ] **Băm Mật khẩu**: Sử dụng **Argon2id** để lưu trữ mật khẩu.
    - [ ] Cấu hình: Memory cost > 64MB, Time cost > 1s tính toán.
    - [ ] Fallback cho hệ thống cũ: **bcrypt** với work factor **≥ 12**.
- [ ] **Tuân thủ OAuth 2.1**:
    - [ ] **PKCE (Proof Key for Code Exchange)** được kích hoạt cho **tất cả** client (Confidential & Public).
    - [ ] **Cấm Implicit Flow** (`response_type=token` bị cấm).
    - [ ] **Khớp Chính xác** (Exact Match) cho tất cả Redirect URI (không dùng wildcard).
    - [ ] **Xoay vòng Refresh Token** cho public clients; hủy hiệu lực token cũ ngay lập tức sau khi sử dụng.
- [ ] **MFA**: Bắt buộc hỗ trợ WebAuthn/Passkeys. Ưu tiên khóa phần cứng chống lừa đảo hoặc xác thực nền tảng (platform authenticators) hơn là SMS OTP.

## 2. Bảo mật API (REST, GraphQL, gRPC)
- [ ] **Tổng quát**:
    - [ ] **Rate Limiting**: Triển khai giới hạn theo token-bucket dựa trên IP/User. Sử dụng Redis/Memcached để quản lý trạng thái phân tán.
    - [ ] **Chống Broken Object Level Authorization (BOLA)**: Xác minh rằng **mọi** truy cập cơ sở dữ liệu yêu cầu tài nguyên theo ID đều kiểm tra quyền sở hữu/phân quyền của `current_user`.
- [ ] **Dành cho GraphQL**:
    - [ ] **Vô hiệu hóa Introspection** trong môi trường production.
    - [ ] **Vô hiệu hóa Gợi ý Trường** (Field Suggestions - vd: "Did you mean...?") trong production.
    - [ ] **Giới hạn Độ sâu Truy vấn**: Thực thi độ sâu tối đa (vd: 5-10 cấp).
    - [ ] **Phân tích Độ phức tạp**: Từ chối các truy vấn vượt quá ngưỡng chi phí tính toán được quy định.
- [ ] **Dành cho gRPC**:
    - [ ] Bắt buộc **mTLS** (Mutual TLS) cho tất cả giao tiếp service-to-service.
    - [ ] Thực thi xác thực chứng chỉ (ClientAuth: RequireAndVerifyClientCert).

## 3. Mật mã & Bảo vệ Dữ liệu
- [ ] **Sẵn sàng Hậu Lượng tử (PQC)**:
    - [ ] Kiểm kê toàn bộ việc sử dụng mật mã (khóa, chứng chỉ, giao thức).
    - [ ] Chuyển đổi trao đổi khóa sang các thuật toán kháng lượng tử (ví dụ: lai ghép **ML-KEM** / X25519).
- [ ] **Bảo mật Đường truyền**:
    - [ ] Bắt buộc **TLS 1.3**.
    - [ ] Vô hiệu hóa các phiên bản TLS cũ (1.0, 1.1, 1.2 nếu có thể) và các ciphers yếu (RC4, 3DES).
    - [ ] Kích hoạt **HSTS** (HTTP Strict Transport Security) với `includeSubDomains` và `preload`.
- [ ] **Dữ liệu khi Nghỉ**:
    - [ ] Mã hóa các cột nhạy cảm (PII, tokens) sử dụng **AES-256-GCM**.
    - [ ] Quản lý Khóa: Xoay vòng Khóa Mã hóa Dữ liệu (DEK) thường xuyên; không bao giờ hardcode khóa trong mã nguồn.

## 4. Kiểm soát Đầu vào & Chống Tiêm nhiễm
- [ ] **SQL Injection**:
    - [ ] Sử dụng ORM / Query Builders cho 100% các truy vấn.
    - [ ] **Kiểm toán Truy vấn Thuần (Native Queries)**: Review thủ công mọi mã SQL thuần hoặc annotation `@Query`. Đảm bảo tham số hóa nghiêm ngặt.
- [ ] **Xử lý Đầu vào AI/LLM**:
    - [ ] **Làm sạch (Sanitization)**: Loại bỏ các ký tự điều khiển và HTML khỏi đầu vào người dùng trước khi đưa vào prompt LLM.
    - [ ] **Sandboxing**: Không bao giờ `eval()` hoặc thực thi mã do LLM sinh ra mà không có sandbox cô lập an toàn (ví dụ: gVisor, Firecracker).
    - [ ] **Bảo vệ System Prompt**: Sử dụng dấu phân cách (ví dụ: `"""`) để tách biệt hướng dẫn hệ thống và dữ liệu người dùng.

## 5. DevSecOps & Chuỗi Cung ứng (SLSA)
- [ ] **Quản lý Phụ thuộc**:
    - [ ] Tạo **SBOM** (Software Bill of Materials) cho mỗi bản build (chuẩn CycloneDX/SPDX).
    - [ ] Sử dụng công cụ tự động (Dependabot/Renovate) với chính sách vá lỗi tức thì cho các CVE nghiêm trọng.
    - [ ] Ghim (Pin) các phụ thuộc vào phiên bản chính xác hoặc mã băm (lockfiles), không dùng khoảng (ranges).
- [ ] **Bảo mật CI/CD**:
    - [ ] **Signed Commits**: Bắt buộc ký GPG cho tất cả các commit git.
    - [ ] **Ký Artifact**: Ký các Docker image và binary (ví dụ: Cosign/Sigstore). Xác minh chữ ký tại thời điểm triển khai (Admission Controllers).
    - [ ] **Quản lý Bí mật**: Không để bí mật trong mã nguồn. Sử dụng Vault, AWS Secrets Manager, hoặc Sealed Secrets.

## 6. Bảo mật Container & Hạ tầng
- [ ] **Làm cứng Container**:
    - [ ] **Non-Root User**: Đảm bảo `USER <id>` được định nghĩa trong Dockerfile (không dùng 0/root).
    - [ ] **Read-Only Root Filesystem**: Cấu hình container chạy với root FS chỉ đọc ở những nơi có thể.
    - [ ] **Distroless Images**: Sử dụng base image tối giản (ví dụ: `gcr.io/distroless/static`) để loại bỏ shell và trình quản lý gói.
- [ ] **Ngữ cảnh Kubernetes**:
    - [ ] `allowPrivilegeEscalation: false`
    - [ ] `runAsNonRoot: true`
    - [ ] Loại bỏ tất cả capabilities (DROP: ["ALL"]).

## 7. Ghi Nhật ký & Giám sát
- [ ] **Structured Logging**: Xuất nhật ký định dạng JSON để phân tích tự động.
- [ ] **Che giấu PII**: Triển khai middleware để tự động che giấu/băm các trường nhạy cảm (email, thẻ tín dụng, auth tokens) **trước** khi ghi log.
- [ ] **Tính Bất biến**: Chuyển nhật ký đến kho lưu trữ tập trung, chống giả mạo (WORM storage).
- [ ] **Correlation IDs**: Theo dõi request xuyên suốt các microservices bằng `X-Request-ID` duy nhất.

## 8. HTTP Security Headers
- [ ] `Content-Security-Policy`: Mặc định là `default-src 'self'`. Sử dụng `nonces` cho inline scripts; tránh `unsafe-inline`.
- [ ] `Strict-Transport-Security`: `max-age=63072000; includeSubDomains; preload`
- [ ] `X-Content-Type-Options`: `nosniff`
- [ ] `X-Frame-Options`: `DENY` hoặc `SAMEORIGIN`
- [ ] `Referrer-Policy`: `strict-origin-when-cross-origin`
- [ ] `Permissions-Policy`: Vô hiệu hóa các tính năng không dùng đến (camera, microphone, geolocation).