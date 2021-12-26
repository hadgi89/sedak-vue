<template>
  <div>
    <el-menu
      class="aside"
      background-color="#343a40"
      text-color="#c2c7d0"
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
  
  .el-menu {
    height: 100vh;
    border: 0;
    background-color: #1c232f;
  }
  
</style>