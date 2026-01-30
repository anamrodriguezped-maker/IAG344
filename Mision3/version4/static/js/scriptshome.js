let datos = [];

document.getElementById("formulario").addEventListener("submit", function(e) {
    e.preventDefault();
    const nombre = document.getElementById("NombreCompleto").value;
    const edad = document.getElementById("edad").value;
    const correo = document.getElementById("correo").value;
    const cargo = document.getElementById("Cargo").value;
    const fecha = document.getElementById("Fecha").value;
    const hora = document.getElementById("Hora").value;
    const salario = document.getElementById("Salario").value;
    const id = document.getElementById("id").value;

    datos.push({
        ID: id,
        Nombre: NombreCompleto,
        Edad: edad,
        Correo: correo,
        Cargo: cargo,
        Fecha: fecha,
        Hora: hora,
        Salario: salario
    });

    this.reset();
    alert("Dato agregado ✔️");
});

function exportarExcel() {
    const hoja = XLSX.utils.json_to_sheet(datos);
    const libro = XLSX.utils.book_new();

    XLSX.utils.book_append_sheet(libro, hoja, "Datos");

    XLSX.writeFile(libro, "datos.xlsx");
}