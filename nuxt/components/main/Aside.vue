<template>
  <div class="aside-wrapper">
    <el-menu
      class="aside"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      
      <el-menu-item index="1">
        <i class="el-icon-s-management"></i>
        <span>Проекты</span>
      </el-menu-item>

      <el-menu-item index="2">
        <i class="el-icon-s-cooperation"></i>
        <span>Должники</span>
      </el-menu-item>
      
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-s-promotion"></i>
          <span>Корреспонденция</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="3-1">Входящая</el-menu-item>
          <el-menu-item index="3-2">Исходящая</el-menu-item>
          <el-menu-item index="3-3">Корреспонденты</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <!-- 
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>Navigator One</span>
        </template>
        <el-menu-item-group title="Group One">
          <el-menu-item index="1-1">item one</el-menu-item>
          <el-menu-item index="1-2">item one</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="Group Two">
          <el-menu-item index="1-3">item three</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <template slot="title">item four</template>
          <el-menu-item index="1-4-1">item one</el-menu-item>
        </el-submenu>
      </el-submenu>
      -->
      
      <el-menu-item index="4">
        <i class="el-icon-s-tools"></i>
        <span>Разное</span>
      </el-menu-item>
      
    </el-menu>
  </div>
</template>


<script>
export default {
  name: "Aside",
}
</script>

<style lang="css" scoped>
  .aside-wrapper {
    height: 100vh;
  }
  .aside {
    height: 100%;
  }
</style>