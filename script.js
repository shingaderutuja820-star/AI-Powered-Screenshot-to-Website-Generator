const fileInput =
    document.getElementById("screenshot");

const preview =
    document.getElementById("preview");


fileInput.addEventListener(
    "change",
    function () {

        const file = this.files[0];

        if (!file) {
            return;
        }

        const reader = new FileReader();

        reader.onload = function (event) {

            preview.innerHTML =
                `<img src="${event.target.result}"
                alt="Screenshot Preview">`;

        };

        reader.readAsDataURL(file);

    }
);


async function generateWebsite() {

    const file = fileInput.files[0];

    if (!file) {

        alert(
            "Please upload a screenshot first."
        );

        return;
    }


    const formData = new FormData();

    formData.append(
        "screenshot",
        file
    );


    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/generate",
                {
                    method: "POST",
                    body: formData
                }
            );


        const result =
            await response.json();


        document.getElementById(
            "htmlCode"
        ).value = result.html;


        document.getElementById(
            "cssCode"
        ).value = result.css;


        const page =
            result.html +
            "<style>" +
            result.css +
            "</style>";


        document.getElementById(
            "websitePreview"
        ).srcdoc = page;

    }

    catch (error) {

        console.error(error);

        alert(
            "Unable to connect with Python server."
        );
    }
}