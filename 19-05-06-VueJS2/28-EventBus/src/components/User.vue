<template>
<div class="component">
  <h1>The User Component</h1>
  <p>I'm an awesome User!</p>
  <button v-on:click="changeName">Change My Name</button>
  {{ name }}
  <hr>
  <div class="row">
    <div class="col-xs-12 col-sm-6">
      <!-- Passing a property dynamically from data -->
      <!-- Listening to changes from the child component -->
      <app-user-detail v-bind:name="name"
                      v-on:nameWasReset="name=$event.name"
                      v-bind:userAge="age"
                      ></app-user-detail>
    </div>
    <div class="col-xs-12 col-sm-6">
      <app-user-edit
        v-bind:userAge="age"
        v-on:ageWasEditted="age=$event.age"
      ></app-user-edit>
    </div>
  </div>
</div>
</template>

<script>
import { eventBus } from '../main'
import UserDetail from './UserDetail.vue';
import UserEdit from './UserEdit.vue';

export default {
  data: function() {
    return {
      name: 'Wojciech',
      age: 27
    }
  },
  methods: {
    changeName() {
      this.name = 'Changed';
      eventBus.$emit('nameWasReset', {name: this.name});
    }
  },
  components: {
    appUserDetail: UserDetail,
    appUserEdit: UserEdit
  },
  created() {
    eventBus.$on('nameWasReset', (eventName) => {
      this.userAge = eventName.name;
    });
    eventBus.$on('nameWasReset', (eventName) => {
      this.name = eventName.name;
    });
  }
}
</script>

<style scoped>
div {
  background-color: lightblue;
}
</style>
