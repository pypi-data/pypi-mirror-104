<template>
  <article v-if='$debug'>
    <div class='article'>
      <h1>Vuex State</h1>
      <ul id='vuex-state'>
        <li class='mb-2' v-for='[k, v] of Object.entries($store.state)' v-if="k != 'context'">
          {{ k }}: {{ v }}
        </li>
        <li class='mb-2' v-for='[k, v] of Object.entries(contextOrEmpty)'>
          context.{{ k }}: {{ v }}
        </li>
      </ul>
    </div>
    <div v-if='hasRouter' class='router'>
      <h1>Vue Router</h1>
      <ul>
        <li class='mb-2'>$route: {name: "{{$route.name}}", path: "{{$route.path}}", query: {{$route.query}} } </li>
        <li class='mb-2'>$router.options.base: "{{ $router.options.base }}" </li>
        <li class='mb-2'>$router.options.routes
          <ul>
            <li v-for='r of $router.options.routes'>{{ r }}</li>
          </ul>
        </li>
      </ul>
    </div>
  </article>
</template>

<style scoped>
  .article {
    color: #4904b3;
    word-break: break-all;
    margin-right: 32px;
  }
  .router {
    color: #138535;
    word-break: break-all;
    margin-right: 32px;
  }
</style>

<script lang="babel">
  export default {
    computed: {
      ...mapVuexItems (),
      contextOrEmpty () {
        return this.context || {}
      },
      hasRouter () {
        return !!router
      }
    },
  }
</script>
