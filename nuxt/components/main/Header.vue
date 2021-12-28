<template>
  <div class="header-wrapper">

    <el-dropdown trigger="click">
      <span class="el-dropdown-link">
        <el-avatar :size="40" src="img/user/avatar-2.jpg"></el-avatar>
        <span>
          <span class="user-name">Joseph William</span>
          <span class="user-desc">Administrator</span>
        </span>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-user"></i> -->
          <i class="material-icons-two-tone">account_circle</i>
          My Account
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-setting"></i> -->
          <i class="material-icons-two-tone">settings</i>
          Settings
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-coin"></i> -->
          <i class="material-icons-two-tone">support</i>
          <span>Support</span>
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-monitor"></i> -->
          <i class="material-icons-two-tone">lock</i>
          Lock 
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-notebook-2"></i> -->
          <i class="material-icons-two-tone">chrome_reader_mode</i>
          Logout
        </el-dropdown-item>
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
    color: #90A4AE;
  }

  .el-dropdown-link {
    color: #546E7A;
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
    color: #7E57C2; 
    background: #E8EAF6;
    cursor: pointer;
  }

  .el-dropdown-menu {
    width: 150px;
  }

  .el-dropdown-item {
    display: block;
    flex-direction: row;
    align-items: center ;
    /* width: 100%; */
    /* padding: 10px 25px; */
    /* clear: both; */
    font-weight: 400;
    /* color: #293240; */
    /* text-align: inherit; */
    /* white-space: nowrap; */
    background-color: blueviolet;
    /* border: 0; */
  }

  .dropdown-item span {
    /* align-self: center; */
    /* margin-top: 20px; */
    /* padding-top: 20px; */
  }

  .dropdown-item.active, 
  .dropdown-item:active,
  .dropdown-item:hover, 
  .dropdown-item:focus {
    color: #7E57C2;
    text-decoration: none;
    background-color: #E8EAF6;
}

i.material-icons-two-tone {
    background-color: #293240;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    /* background-color: #20be7c; */
    vertical-align: middle;
    margin-bottom: 3px;
}

  
</style>