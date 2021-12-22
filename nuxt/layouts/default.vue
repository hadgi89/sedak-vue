<template>
  <el-container >
    
    <el-aside><Aside /></el-aside>
    
    <el-container>
      
      <el-header><Header/></el-header>
      
      <el-main>
        <nuxt/>
      </el-main>
      
      <el-footer>Footer</el-footer>
    
    </el-container>
  </el-container>
</template>


<script>
import Aside from '@/components/main/Aside'
import Header from '@/components/main/Header'
import Footer from '@/components/main/Footer'

export default {
  components: {Aside, Header, Footer}
}
</script>


<style scoped>
  
  el-aside {
    /* height: 100%; */
    width: 240px;
  }
</style>