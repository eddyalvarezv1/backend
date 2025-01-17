import express from "express";
import { usuarioEnrutador } from "./routes/usuario.routes.js";
import { ZodError } from "zod";
import { Prisma } from "@prisma/client";

const servidor = express();
servidor.use(express.json());

// Agregamos las rutas de nuestros enrutadores
servidor.use(usuarioEnrutador);

servidor.use((error, req, res, next) => {
    // Aca manejaremos los errores que podamos teber en todas nuestra aplicacion
    // Para mejorar el error global se tiene que declarar LUEGO de todas las rutas sino evitara que ingrese al controlador adecuado
    if (error instanceof ZodError) {
        return res.status(400).json({
            message: "Error al recibir la información",
            content: error.errors,
        });
    }
    if (error instanceof Prisma.PrismaClientInitializationError) {
        // la clase PrismaClientInitializationError tiene la propiedad meta en la cual almacena el modelo que emitio el error al no encontrar la coincidencia en la bd
        return res.status(404).json({
            message: `El ${error.meta.modelName} no existe`,
        })
    }

    return res.status(400).json({
        message: "Error al hacer la petición",
    });
});

servidor.listen(process.env.PORT, () => {
    console.log(
        `Servidor corriendo exitosamente en el puerto${process.env.PORT}`
    );
});