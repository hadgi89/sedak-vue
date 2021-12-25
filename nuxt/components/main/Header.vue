<template>
  <div class="header-wrapper">
    <!-- <el-dropdown trigger="click">
      <el-button type="primary">
        <div class="user-wrapper">
          <div>
            <div>Joseph William</div>
            <div>Administrator</div>
          </div>
          <el-avatar :size="50" src="img/user/avatar-2.jpg"></el-avatar>
        </div>
      </el-button>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>Action 1</el-dropdown-item>
        <el-dropdown-item>Action 2</el-dropdown-item>
        <el-dropdown-item>Action 3</el-dropdown-item>
        <el-dropdown-item>Action 4</el-dropdown-item>
        <el-dropdown-item>Action 5</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown> -->

    <el-dropdown trigger="click">
      <span class="el-dropdown-link">
        <el-avatar :size="40" src="img/user/avatar-2.jpg"></el-avatar>
        <span>
          <span class="user-name">Joseph William</span>
          <span class="user-desc">Administrator</span>
        </span>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item class="dropdown-item">My Account</el-dropdown-item>
        <el-dropdown-item class="dropdown-item">Settings</el-dropdown-item>
        <el-dropdown-item>Support</el-dropdown-item>
        <el-dropdown-item>Lock Screen</el-dropdown-item>
        <el-dropdown-item>Logout</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>

  
  
  </div>
</template>


<script>
  export default {
    name: "Header",
  }
</script>


<style lang="css" scoped>

  .header-wrapper {
    display: inline-flex;
    align-items: center;
    justify-content: flex-end;
    width: 100%;
    height: 100%;
    background-color: #FFFFFF;
  }

  .el-avatar {
    margin-right: 10px;
  }
  .user-name {
    display: block;
    line-height: 1;
    margin-bottom: 5px;
    font-size: 15px;
    font-weight: 600;
  }

  .user-desc {
    display: block;
    line-height: 1;
    font-size: 12px;
    font-weight: 400;
    color: #525b69b3;
  }

  .el-dropdown-link {
    color: #525b69;
    display: inline-flex;
    align-items: center;
    padding: 0.60rem 0.9rem;
    margin: 0 5px;
    border-radius: 4px;
    position: relative;
    font-weight: 500;
  }

  .el-dropdown-link.active, 
  .el-dropdown-link:active, 
  .el-dropdown-link:focus, 
  .el-dropdown-link:hover {
    text-decoration: none;
    color: #7267EF;
    background: #e3e1fc;
    cursor: pointer;
  }

  .el-dropdown-menu {
    width: 150px;
  }

  .dropdown-item {
    display: block;
    /* width: 100%; */
    /* padding: 0.65rem 1.5rem; */
    /* clear: both; */
    font-weight: 400;
    /* color: #293240; */
    /* text-align: inherit; */
    /* white-space: nowrap; */
    /* background-color: transparent; */
    /* border: 0; */
  }

  .dropdown-item.active, 
  .dropdown-item:active,
  .dropdown-item:hover, 
  .dropdown-item:focus {
    color: #7267ef;
    text-decoration: none;
    background-color: #e3e1fc;
}



  
</style>