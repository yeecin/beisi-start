<template>
  <div class="login">
    <div class="login-mask"></div>
    <div class="login-box">
      <!-- 右侧表单 -->
      <div class="login-box-form">
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
/* 样式与之前保持一致 */
</style>