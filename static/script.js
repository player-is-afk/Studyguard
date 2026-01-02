document.addEventListener("DOMContentLoaded", () => {
    const response = document.getElementById("response-text");
    if (response) {
        const text = response.textContent;
        response.textContent = "";
        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                response.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 10); // adjust typing speed
            }
        }
        typeWriter();
    }
});
