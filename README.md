# WeatherWatch Pro：專案計劃（使用 Line 通知）

## 專案概述

WeatherWatch Pro 是一個天氣資訊服務，允許用戶查詢當前天氣數據、預報，並訂閱個人化的天氣警報。該系統將從多個天氣 API 聚合數據，提供用戶認證，並通過 Line 發送基於訂閱的天氣警報。

## 技術棧

- 後端：Python 與 FastAPI 框架
- 資料庫：PostgreSQL
- 認證：JSON Web Tokens (JWT)
- 外部 API：OpenWeatherMap、WeatherAPI.com
- 消息隊列：Redis
- 通知服務：Line Messaging API
- 測試：Pytest
- API 文檔：Swagger/OpenAPI

## 系統架構

1. API 層：FastAPI REST API
2. 認證服務：基於 JWT 的認證系統
3. 天氣數據服務：從外部 API 獲取和聚合數據
4. 訂閱服務：管理用戶訂閱和偏好設置
5. 通知服務：基於用戶偏好通過 Line 發送天氣警報
6. 資料庫層：PostgreSQL 用於存儲用戶數據、訂閱和緩存的天氣數據
7. 消息隊列：Redis 用於處理異步任務

## 專案任務

### 1. 專案設置和基本結構

- [x] 初始化 Python 專案並安裝依賴
- [x] 使用 FastAPI 設置基本路由
- [x] 配置 PostgreSQL 連接
- [x] 實現基本錯誤處理中間件

### 2. 用戶認證系統

- [x] 設計用戶模型（用戶名、電子郵件、Line 用戶 ID 等）
- [x] 實現用戶註冊端點
- [x] 實現用戶登錄端點並生成 JWT
- [x] 創建用於使用 JWT 認證路由的中間件
- [x] 實現密碼重置功能

### 3. Line 整合

- [x] 註冊 Line Developer 帳號並創建 Line Bot
- [ ] 實現 Line 登錄功能，獲取用戶 Line ID
- [ ] 創建 Line 消息發送服務
- [ ] 實現接收和處理來自用戶的 Line 消息的端點

### 4. 天氣數據聚合

- [ ] 設置與外部天氣 API 的連接
- [ ] 創建獲取當前天氣數據的服務
- [ ] 實現從多個來源聚合數據
- [ ] 創建天氣數據的緩存機制
- [ ] 設計並實現獲取天氣數據的端點

### 5. 訂閱系統

- [ ] 設計訂閱模型（用戶、偏好、頻率等）
- [ ] 實現創建和管理訂閱的端點
- [ ] 創建處理訂閱和用戶偏好的服務

### 6. 通知服務

- [ ] 設置 Redis 用於消息隊列
- [ ] 實現處理隊列通知的工作者
- [ ] 整合 Line Messaging API 以發送天氣通知
- [ ] 創建檢查天氣和觸發警報的定時任務

### 7. API 端點

- [ ] `/auth`：註冊、登錄、Line 帳號綁定
- [ ] `/weather`：獲取當前天氣、預報
- [ ] `/subscriptions`：用戶訂閱的 CRUD 操作
- [ ] `/profile`：用戶資料管理
- [ ] `/line-webhook`：處理來自 Line 的事件和消息

### 8. 測試

- [ ] 為每個服務編寫單元測試
- [ ] 使用 Pytest 實現 API 端點的集成測試
- [ ] 創建測試資料庫和測試固件
- [ ] 模擬 Line API 調用進行測試

### 9. 文檔

- [ ] 使用 Swagger/OpenAPI 設置 API 文檔
- [ ] 記錄所有 API 端點和請求/響應格式
- [ ] 創建包含專案概述和設置說明的 README
- [ ] 編寫 Line Bot 使用指南

### 10. 優化和安全性

- [ ] 實現 API 請求的速率限制
- [ ] 設置輸入驗證和淨化
- [ ] 優化資料庫查詢並實現索引
- [ ] 實現 HTTPS 和安全標頭
- [ ] 確保 Line 消息的安全處理

### 11. 部署

- [ ] 設置部署管道（例如，GitHub Actions）
- [ ] 配置生產環境變量
- [ ] 部署到雲平台（例如，Heroku、AWS）
- [ ] 設置 Line Bot 的公開 URL

## 進階目標

- 實現多語言支持
- 整合額外的天氣數據來源
- 添加自定義天氣警報條件
- 實現天氣相關的 Line 互動遊戲或測驗
