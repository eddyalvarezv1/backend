import { registrarUsuarioSerializer } from "./seriallizers/usuario_seriallizer.js"

export const registrarUsuarioSerializer = async (req, res) => {
    const data = req.body;
    // Valida si la información es valida o no
    const dataValidada = registrarUsuarioSerializer.parse(data);
    console.log(dataValidada);

    return res.json({
        message: "Usuario registrado exitosamente",
    });
};