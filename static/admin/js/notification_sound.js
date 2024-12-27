document.addEventListener("DOMContentLoaded", function () {
    function playNotificationSound() {
        const audio = new Audio('/static/sounds/notification.mp3'); // Убедитесь, что путь к файлу корректен
        audio.play();
    }

    async function checkNotifications() {
        try {
            const response = await fetch('/check-notifications/');
            if (response.ok) {
                const data = await response.json();
                if (data.new_notifications) {
                    playNotificationSound();
                }
            }
        } catch (error) {
            console.error("Ошибка при проверке уведомлений:", error);
        }
    }

    // Проверяем уведомления каждые 10 секунд
    setInterval(checkNotifications, 10000);
});
