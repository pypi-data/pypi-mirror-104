<template>
  <el-row :gutter="0" class="elevation-3 px-5">
    <el-col :xs=12 :sm=6 id='logo'>
      <h3 class='green--text text--lighten-5 pl-5 mt-4'>HTTP-SFC</h3>
    </el-col>

    <el-col :xs=0 :sm=12>
      <el-menu
        :default-active="navbarActiveIndex"
        class="el-menu"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        height="50">

        <el-submenu index="1">
        <template slot="title">Templates</template>
        <a href="/examples"><el-menu-item index="1-1">Index</el-menu-item></a>
        <a href="/examples/todos"><el-menu-item index="1-2">Template 1</el-menu-item></a>
        <a href="/examples/router"><el-menu-item index="1-3">Template 2</el-menu-item></a>
        <a href="/examples/tutorial"><el-menu-item index="1-3">Tutorial</el-menu-item></a>
        </el-submenu>

        <el-submenu index="2">
        <template slot="title">Menu 2</template>
        <el-menu-item index="2-1">item one</el-menu-item>
        <el-menu-item index="2-2">item two</el-menu-item>
        <el-menu-item index="2-3">item three</el-menu-item>
        <el-submenu index="2-4">
          <template slot="title">item four</template>
          <el-menu-item index="2-4-1">item one</el-menu-item>
          <el-menu-item index="2-4-2">item two</el-menu-item>
          <el-menu-item index="2-4-3">item three</el-menu-item>
        </el-submenu>
        </el-submenu>
        <el-menu-item index="3" disabled>Menu 3</el-menu-item>
      </el-menu>
    </el-col>

    <el-col :xs=12 :sm=6 class="text-right pt-3">
      <div class="text-no-wrap size-12 w-700 lime--text text--darken-1">{{ $user ? $user.nick_name : "Guest" }}</div>
      <a v-if="$user" :href="`/auth/signout?return_url=${$location.href}`"><span class="text-no-wrap size-11 w-700 grey--text text--lighten-2">Sign Out</span></a>
      <a v-else :href="`/auth/signin?return_url=${$location.uri}`"><span class="text-no-wrap size-11 w-700 grey--text text--lighten-2">Sign In</span></a>
    </el-col>

  </el-row>
</template>

<script lang="babel">
  export default {
    computed: {
      ...mapVuexItems (),
    }
  }
</script>
