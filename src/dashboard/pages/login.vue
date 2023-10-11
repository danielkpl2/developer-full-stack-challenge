<template>
    <div class="container mt-5">
        <b-form @submit="login">
            <b-form-group label="Username" label-for="username" label-align="left">
                <b-form-input id="username" v-model="username" type="text" required></b-form-input>
            </b-form-group>

            <b-form-group label="Password" label-for="password" label-align="left">
                <b-form-input id="password" v-model="password" type="password" required></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary">Login</b-button>
            <div class="loggedin">{{ this.$auth.loggedIn ? "Logged in" : "Not logged in" }}</div>
        </b-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async login(event) {
            event.preventDefault();
            try {
                const form = new FormData()
                form.append("username", this.username)
                form.append("password", this.password)
                form.append("grant_type", 'password')

                const response = await this.$auth.loginWith('local', {
                    data: form
                });
                this.$router.push('/authors');

            } catch (error) {
                console.error('Login failed', error);
            }
        },
    },
};
</script>