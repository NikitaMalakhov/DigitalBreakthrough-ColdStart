<template>
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">{{ video_data.title }}</h3>
        </div>
        <div class="card-body">
            <span class="card-duration">{{ minutesToHHMM(video_data.v_duration) }}</span>
            <p>{{ video_data.category_id }}</p>
            <p class="card-views">{{ video_data.v_year_views }} views</p>
        </div>
        <div class="card-footer">
            <div class="likes-dislikes">
                <button @click="likeVideo(video_data.video_id)" class="btn like-btn">👍 {{ video_data.v_likes }}</button>
                <button @click="dislikeVideo(video_data.video_id)" class="btn dislike-btn">👎 {{ video_data.v_dislikes }}</button>
            </div>
        </div>
    </div>
</template>


<script lang="ts">
import Video from '@/interfaces/video';
import { useHomePageStore } from '@/stores/homepage';
import axios from 'axios';



export default {
    props: {
        video_data: {
            type: Object as () => Video
        }
    },

    data() {
        return {
        };
    },
    methods: {
        minutesToHHMM(minutes) {
            const hours = Math.floor(minutes / 60);
            const mins = Math.floor(minutes % 60);
            return `${String(hours).padStart(2, '0')}:${String(mins).padStart(2, '0')}`;
        },
        async likeVideo(videoId: string) {
            let store = useHomePageStore();
            store.likeVideo(videoId);
            const session_id = await localStorage.getItem('session_id');
            const response = await axios.post(`http://127.0.0.1:8000/api/${videoId}/like?session_id=${session_id}`);
        },
        async dislikeVideo(videoId: string) {
            let store = useHomePageStore();
            store.dislikeVideo(videoId);
            const session_id = await localStorage.getItem('session_id');

            const response = await axios.post(`http://127.0.0.1:8000/api/${videoId}/dislike?session_id=${session_id}`);
        }
    }
}
</script>


<style scoped>
.card {
    height: 200px;
    background-color: #ffffff;
    /* Card background */
    border: 1px solid #ccc;
    color: black;

    /* Card border */
    border-radius: 8px;
    /* Rounded corners */
    padding: 20px;

    /* Inner padding */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    /* Shadow effect */
    transition: transform 0.2s;
    /* Smooth transition for hover effect */
    display: flex;
    flex-direction: column;
    /* Stack elements vertically */
    justify-content: space-between;
    /* Space between header, body, and footer */
}

.card:hover {
    transform: scale(1.05);
    /* Scale effect on hover */
}

.card-header {
    font-size: 10px;
    display: flex;
    justify-content: space-between;
    /* Space between title and duration */
    align-items: center;
    /* Align items vertically */
}

.card-title {
    font-size: 1.2em;
    /* Font size for the title */
    margin: 0;
    /* Remove default margin */
}

.card-duration {
    font-size: 0.9em;
    /* Smaller font size for duration */
    color: #666;
    /* Lighter color for duration */
}

.card-body {

    margin-top: 10px;
    /* Space above views text */
}

.card-views {
    font-size: 0.9em;
    /* Font size for views */
    color: #666;
    /* Lighter color for views */
}

.card-footer {
    margin-top: 10px;
    /* Space above footer */
    display: flex;
    justify-content: center;
    /* Center the buttons */
    align-items: center;
    /* Align items vertically */
}

.likes-dislikes {
    display: flex;
    /* Align buttons in a row */
    gap: 10px;
    /* Space between buttons */
}

.btn {
    padding: 8px 12px;
    /* Padding for buttons */
    border: none;
    /* Remove default border */
    border-radius: 5px;
    /* Rounded corners */
    cursor: pointer;
    /* Pointer cursor on hover */
    font-size: 0.9em;
    /* Font size for buttons */
}

.like-btn {
    background-color: #4caf50;
    /* Green background for like button */
    color: white;
    /* White text color */
}

.dislike-btn {
    background-color: #f44336;
    /* Red background for dislike button */
    color: white;
    /* White text color */
}
</style>
