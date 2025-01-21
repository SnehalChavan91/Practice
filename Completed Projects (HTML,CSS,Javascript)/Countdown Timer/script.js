document.getElementById('start').addEventListener('click', function() {
    const targetDate = new Date(document.getElementById('datetime').value).getTime();

    if (isNaN(targetDate)) {
        alert("Please select a valid date and time.");
        return;
    }

    function updateCountdown() {
        const now = new Date().getTime();
        const timeRemaining = targetDate - now;

        if (timeRemaining <= 0) {
            clearInterval(interval);
            document.getElementById('countdown').innerHTML = '<p>Time is up!</p>';
            return;
        }

        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        document.getElementById('days').innerText = days;
        document.getElementById('hours').innerText = hours;
        document.getElementById('minutes').innerText = minutes;
        document.getElementById('seconds').innerText = seconds;
    }

    updateCountdown();
    const interval = setInterval(updateCountdown, 1000);
});