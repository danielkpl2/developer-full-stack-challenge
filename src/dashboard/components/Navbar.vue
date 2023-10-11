<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">Datacose</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item href="#"><NuxtLink to="/authors">Authors</NuxtLink></b-nav-item>
                    <b-nav-item href="#"><NuxtLink to="/books">Books</NuxtLink></b-nav-item>
                </b-navbar-nav>

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <b-nav-item><NuxtLink to="/login">Login</NuxtLink></b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<style scoped>
a {
    color: white;
}
</style>