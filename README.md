# beisi-start

全栈开发者的第一个练习

### 任务书

- 任务描述

  fork 本仓库，并基于本仓库开发一个前后端分离的简单登录系统，要求前端提供登录页面，后端提供登录接口，前端通过 API 调用进行登录验证

  备注：需要将源代码提交至 fork 后的仓库，并将作品部署到服务器上。

- 功能要求

  - 前端部分

    - 实现一个登录页面，包括：
      - 输入框：用户名
      - 输入框：密码
      - 登录按钮
    - 点击登录按钮后：
      - 将用户名和密码发送到后端 API
      - 根据后端返回结果进行提示（登录成功或失败）
      - 登录成功后显示欢迎信息（如："欢迎，xxx"）

  - 后端部分

    - 提供一个 API 接口 /api/login，支持 POST 请求。
    - 接口要求：
      - 接收前端传来的用户名和密码
      - 校验账号密码是否正确（可以硬编码，如 admin/123456）
      - 正确返回登录成功信息和模拟 Token（如随便生成的字符串或 UUID）
      - 错误返回登录失败提示
    - 返回数据格式（统一 JSON 结构）：

      - 成功示例：

        ```json
        {
          "code": 0,
          "message": "Login successful",
          "data": {
            "token": "abcdef123456"
          }
        }
        ```

      - 失败示例：

        ```json
        {
          "code": 1,
          "message": "Invalid username or password",
          "data": null
        }
        ```

- 技术要求

  - 前端：可以使用原生 HTML/CSS/JavaScript，或使用任意框架（Vue、React 均可），自行选择。
  - 后端：使用任意熟悉的技术栈（如 Node.js+Express、Python+Flask、Java+Spring Boot 等）。
  - 数据可以保存在服务器内存中，无需接数据库。
  - 完成前后端之后，需要部署到服务器上供用户访问（使用 IP 地址或域名）。

- 其他要求

  - 前端必须通过 HTTP 请求调用后端接口，禁止在前端直接写账号密码或硬编码模拟登录。
  - 后端必须能独立运行，提供接口访问。
  - 接口文档清晰，说明每个接口的请求方式、参数、返回示例。
  - 前端有基本的错误提示（如用户名密码错误时提示用户）。
  - 前端/后端代码需要注意基本的代码规范与结构。

- 验收标准

  | 项目       | 说明                                       |
  | ---------- | ------------------------------------------ |
  | 前端功能   | 页面完整，能正常调用接口登录               |
  | 后端功能   | 正确验证登录信息并返回符合规范的 JSON 数据 |
  | 前后端交互 | 接口联调顺畅，无硬编码假数据               |
  | 错误处理   | 登录失败时有清晰提示                       |
  | 部署       | 项目能在公网进行访问                       |
  | 代码规范   | 基本代码规范良好，易读                     |

- 提交物要求

  - 项目部署后的链接，可以使用 IP 地址或域名
  - github 仓库链接（包含前后端代码）

- 其他说明

  - 成功登录返回的 token 可以是随机生成的字符串，或者简单模拟。
  - 前端拿到 token 后可以存储在 localStorage 或其他存储中，以便后续使用。
  - 不要求真正的 Token 鉴权功能（如 JWT 验证），只需模拟登录。

- 附加（加分项）

  - 页面美观简洁（如使用 CSS 美化登录页面）
  - 前端有表单验证（如用户名和密码不能为空）
  - 前端有简单的 loading 效果（比如登录中禁用按钮）
  - 登录后能本地存储 Token（如 localStorage）

### 供参考的登录接口文档

- 接口描述

  用户登录接口，验证用户名和密码，返回登录状态及模拟 Token。

- 请求接口

  - URL：/api/login
  - 请求方式：POST
  - 请求参数类型：application/json

- 请求参数

  | 参数名   | 类型   | 是否必填 | 说明   |
  | -------- | ------ | -------- | ------ |
  | username | string | 是       | 用户名 |
  | password | string | 是       | 密码   |

- 请求示例

  ```json
  {
    "username": "admin",
    "password": "123456"
  }
  ```

- 响应结果

  - 成功响应（账号密码正确）

    - HTTP 状态码：200

      ```json
      {
        "code": 0,
        "message": "Login successful",
        "data": {
          "token": "abcdef123456"
        }
      }
      ```

    - 字段说明

      | 字段名     | 类型   | 说明                   |
      | ---------- | ------ | ---------------------- |
      | code       | int    | 0 表示成功             |
      | message    | string | 提示信息               |
      | data.token | string | 登录成功后的模拟 Token |

  - 失败响应（账号密码错误）

    - HTTP 状态码：200

      ```json
      {
        "code": 1,
        "message": "Invalid username or password",
        "data": null
      }
      ```

    - 字段说明

      | 字段名  | 类型   | 说明               |
      | ------- | ------ | ------------------ |
      | code    | int    | 1 表示失败         |
      | message | string | 错误提示信息       |
      | data    | null   | 登录失败无返回数据 |
