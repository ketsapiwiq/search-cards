<template>
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{ data.title }}</h5>
          <!-- id: {{ card.id }} -->
          <p class="card-text">{{ data.text }}</p>
          <pre class="card-data">{{ data }}</pre>
        </div>
      </div>
</template>

<script>
export default {
  props: ['data'],
  data () {
    return {
    }
  }
}
</script>