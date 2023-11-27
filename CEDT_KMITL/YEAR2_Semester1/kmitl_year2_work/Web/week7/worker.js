// worker.js
self.onmessage = function() {
    setInterval(function() {
        // Get the current date and time
        const date = new Date();
        const time = date.toString();

        const color = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
        const textcolor = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;

        postMessage({time, color, textcolor});
    },1000);
};
