<template>
      <div class="card" v-bind:key="card">
        <div class="card-body">
          <h5 class="card-title">{{ card.data.title }}</h5>
          <!-- id: {{ card.id }} -->
          <p class="card-text">{{ card.data.text }}</p>
          <pre class="card-data">{{ card.data }}</pre>
        </div>
      </div>
</template>

<script>
export default {
  props: ['card'],
  data () {
    return {
    //   card: ''
    }
  }
}
</script>