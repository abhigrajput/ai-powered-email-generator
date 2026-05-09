const button = document.getElementById("generateBtn");

const result = document.getElementById("result");

const loader = document.getElementById("loader");

button.addEventListener("click", async() => {

    const prompt = document.getElementById("emailPrompt").value;

    const emailType = document.getElementById("emailType").value;

    const tone = document.getElementById("tone").value;

    if (prompt.trim() === "") {

        result.innerHTML = "Please enter email details.";

        return;
    }

    loader.style.display = "block";

    result.innerHTML = "";

    try {

        const response = await fetch('/generate', {

            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({
                prompt,
                emailType,
                tone
            })

        });

        const data = await response.json();

        loader.style.display = "none";

        result.innerHTML = data.email.replace(/\n/g, "<br>");

    } catch (error) {

        loader.style.display = "none";

        console.log(error);

        result.innerHTML = "Error generating email.";

    }

});


const copyBtn = document.getElementById("copyBtn");

copyBtn.addEventListener("click", () => {

    const text = document.getElementById("result").innerText;

    navigator.clipboard.writeText(text);

    copyBtn.innerText = "Copied!";

    setTimeout(() => {

        copyBtn.innerText = "Copy Email";

    }, 2000);

});


const downloadBtn = document.getElementById("downloadBtn");

downloadBtn.addEventListener("click", () => {

    const content = document.getElementById("result").innerText;

    const blob = new Blob([content], { type: "text/plain" });

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "generated_email.txt";

    a.click();

});


function setTemplate(type) {

    const prompt = document.getElementById("emailPrompt");

    if (type === "internship") {

        prompt.value =
            "Write a professional internship request email for software developer role.";

    } else if (type === "leave") {

        prompt.value =
            "Write a professional leave request email for fever and health issue.";

    } else if (type === "complaint") {

        prompt.value =
            "Write a complaint email regarding poor internet service.";

    }
}