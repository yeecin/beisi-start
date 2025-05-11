<template>
  <div class="login">
    <div class="login-mask"></div>
    <div class="login-card">
      <!-- 登录/注册表单卡片 -->
      <div class="card-content">
        <el-tabs v-model="ActiveFormType" class="demo-tabs">
          <!-- 登录表单 -->
          <el-tab-pane label="登录" name="login">
            <login-form @toRegister="toRegister" />
          </el-tab-pane>

          <!-- 注册表单 -->
          <el-tab-pane label="注册" name="register">
            <register-form @toLogin="toLogin" />
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import loginForm from "./components/loginForm.vue";
import registerForm from "./components/registerForm.vue";

// 表单类型和标签
const ActiveFormType = ref("login");

// 切换到注册表单
const toRegister = () => {
  ActiveFormType.value = "register";
};

// 切换到登录表单
const toLogin = () => {
  ActiveFormType.value = "login";
};

onMounted(() => sessionStorage.clear());
</script>

<style lang="less" scoped>
.login {
  width: 100%;
  height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f0f2f5;

  // 背景蒙版（如果需要）
  .login-mask {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.1);
    z-index: 1;
  }

  // 登录卡片
  .login-card {
    position: relative;
    z-index: 2;
    width: 400px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    overflow: hidden;

    .card-content {
      padding: 30px;

      // 标签样式
      :deep(.el-tabs__header) {
        margin-bottom: 25px;
      }

      :deep(.el-tabs__nav) {
        width: 100%;
        display: flex;
      }

      :deep(.el-tabs__item) {
        flex: 1;
        text-align: center;
        font-size: 16px;
      }
    }
  }
}

// 移动端响应式设计
@media (max-width: 576px) {
  .login-card {
    width: 90% !important;
    margin: 0 auto;

    .card-content {
      padding: 20px;
    }
  }
}
</style>