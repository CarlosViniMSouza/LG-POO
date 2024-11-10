function ResetForms() {
    document.getElementById("addProduct").addEventListener("click", function() { 
        // Limpa os campos do formulário
        document.getElementById("name").value = ""; 
        document.getElementById("price").value = ""; 
        document.getElementById("category").value = ""; 
    });
}