// Arrow function (funcion tipo flecha)
// funcion anonima

export const sumar = (numero1, numero2) => {
    const resultado = numero1 + numero2;
    return resultado;
};

// funcion tradicional
export function restar(numero1, numero2) {
    const resultado = numero1 - numero2;
    return resultado;
}

// Adicional a ello si la funcion es de una sola linea y retornará el resultado
export const multiplicar =(numero1, numero2) => numero1 * numero2;
