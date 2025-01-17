import express from "express";
import { 
    registrarUsuario,
    login,
    actualizarUsuario,
 } from "../controllers/usuario.controller.js";
import AsyncHandler from "express-async-handler";
import { validarUsuario } from "../controllers/middlewares.js";

export const usuarioEnrutador = express.Router();

// Agregamos todas las rutas relacionadas al usuario
// asyncHandler > captura el controlador asincrono y lo espera para que si, tiene algun error lo podamos manejar en nuestro error handler
usuarioEnrutador.post("/registro", AsyncHandler(registrarUsuario));
usuarioEnrutador.post("/login", AsyncHandler(login));
usuarioEnrutador.put(
    "/actualizar-usuario",
    AsyncHandler(validarUsuario),
    AsyncHandler(actualizarUsuario)
);