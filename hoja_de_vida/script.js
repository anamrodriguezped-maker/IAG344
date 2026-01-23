function downloadPDF(){
   const element = document.querySelector('#pdf-content');
   //console.log(element);
   //alert("Archivo descargando 😎");
    const otp={ 
        marigin:[10, 5, 15, 5],// arriba, izquierda, abajo y derecha en mm
        filename: 'H_V_Ana_Rodriguez.pdf',
        image:{ type: 'jpeg', quality: 1 },
        html2canvas:{ 
            scale: 2, 
            useCORS: true,
            scrollY:0
        },
        jsPDF:{ 
            unit:'mm',
            format: 'a4',
            orientation:'portrait'
        }
    }
    html2pdf().set(otp).from(element).save();
}