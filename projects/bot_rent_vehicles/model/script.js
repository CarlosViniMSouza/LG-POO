function showForms(formsId) {
    const forms = document.querySelectorAll(".form-container");
    forms.forEach((form) => form.classList.remove("active"));

    // Mostrar o formulário selecionado
    document.getElementById(formsId).classList.add("active");

    // Atualizar a aba ativa
    const tabs = document.querySelectorAll(".tab");
    tabs.forEach((tab) => tab.classList.remove("active"));
    const activeTab = Array.from(tabs).find(
        (tab) => tab.innerText === `Insert ${formsId.replace("Form", "")}`
    );
    activeTab.classList.add("active");
}

function saveBasicInfos(event) {
    event.preventDefault();
    const name = document.getElementById("name").value;

    const saveArchive = (content, archiveName) => {
        const blob = new Blob([content], { type: "text/plain" });
        const link = document.createElement("a");

        link.href = URL.createObjectURL(blob);
        link.download = archiveName;
        link.click();
    };

    const archiveContent = `name: ${name}`;
    saveArchive(archiveContent, "dados_name.txt");

    //alert("name salvo com sucesso!");
}

function saveInfosCar(event) {
    event.preventDefault();
    const gasoline = document.getElementById("gasoline").value;

    const saveArchive = (content, archiveName) => {
        const blob = new Blob([content], { type: "text/plain" });
        const link = document.createElement("a");

        link.href = URL.createObjectURL(blob);
        link.download = archiveName;
        link.click();
    };

    const archiveContent = `gasoline: ${gasoline}`;
    saveArchive(archiveContent, "dados_contato.txt");

    //alert("Contato salvo com sucesso!");
}

function saveInfosMotocycle(event) {
    event.preventDefault();
    const year = document.getElementById("year").value;
    const daily_value = document.getElementById("daily_value").value;

    const saveArchive = (content, archiveName) => {
        const blob = new Blob([content], { type: "text/plain" });
        const link = document.createElement("a");
        
        link.href = URL.createObjectURL(blob);
        link.download = archiveName;
        link.click();
    };

    const archiveContent = `year: ${year}\nSenha: ${daily_value}`;
    saveArchive(archiveContent, "dados_login.txt");
}