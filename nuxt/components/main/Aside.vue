<template>
  <div>
    <el-menu class="aside" background-color="#1F2937" text-color="#9CA3AF" active-text-color="#E5E7EB">
      
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
  }
  
</style>