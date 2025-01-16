// Arrow function (funcion tipo flecha)
// funcion anonima

export const sumar = (numero1, numero2) => {
    const resultado = numero1 + numero2;
    return resultado;
}

// funcion tradicional
function restar(numero1, numero2) {
    const resultado = numero1 - numero2;
    return resultado;
}

// Adicional a ello si la funcion es de una sola linea y retornará el resultado
const multiplicar =(numero1, numero2) => numero1 * numero2;

// Segun commomJS para realizar una exportacion se realiza asi

module.exports = {
    sumar: sumar,
    // Si la llave es el mismo nombre que la funcion o variable que se va a llamar se puede omitir
    restar,
    multiplicar,
};