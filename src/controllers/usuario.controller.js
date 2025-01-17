import { conexion } from "../conexion.js";
import { loginSerializer, registrarUsuarioSerializer } from "./seriallizers/usuario_seriallizer.js";
import { genSalt, hash, compare } from "bcrypt";
import JWT from "jsonwebtoken";

export const registrarUsuario = async (req, res) => {
    const data = req.body;
    // Valida si la información es valida o no
    const dataValidada = registrarUsuarioSerializer.parse(data);
    console.log(dataValidada);

    const salt = await genSalt();
    const password = await hash(dataValidada.password, salt);

    const nuevoUsuario = await conexion.usuario.create({
        data: {
            email: dataValidada.email,
            apellido: dataValidada.apellido,
            nombre: dataValidada.nombre,
            password,
            tipoUsuario: dataValidada.tipoUsuario,
        },

        select: {
            id: true,
            email: true,
            apellido: true,
            nombre: true,
            tipoUsuario: true,
        },

    });

    return res.json({
        message: "Usuario registrado exitosamente",
        content: nuevoUsuario,
    });
};

export const login = async (req, res) => {
    const dataValidada = loginSerializer.parse(req.body);

    const usuarioEncontrado = await conexion.usuario.findUniqueOrThrow({
        where: {email: dataValidada.email},
    });

    const esLaPassword = await compare(
        dataValidada.password,
        usuarioEncontrado.password,
    );

    if (esLaPassword) {
        const token = JWT.sign (
            { usuarioId: usuarioEncontrado.id},
            process.env.SECRET_KEY,
            {
                expiresIn: 60 * 60 * 4, // si el valor es un entero será en segundos o "2 days" | "12h" | "4d"
            }
        );

        return res.json({
            message: "Bienvenido",
            content: token,
        });
    }   else {
        return res.status(403).json({
            message: "Credenciales incorrectas",
        });
    }
};

export const actualizarUsuario = async (req, res) => {
    return res.json({
        message: "Usuario actualizado exitosamente",
    });
};