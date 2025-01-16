import express from "express";
// esta liberia se agrega cuando creamos los tipos de primsa
// npx prisma migrate generate
// cuando creamos una nueva migración y se ejecuta en la bd
import Prisma from '@prisma/client';

const conexion = new Prisma.PrismaClient();
const servidor = express();

servidor.use(express.json());

servidor.post("/registro", async (req, res) =>{
    try {
        const data = req.body; // {nombre: '', email'', nickname:''}

        // resultado > seria la ejecucion correcta de la funcion
        const resultado = await conexion.usuario.create({
          data
        });
        // ACA PONES TU MENSAJE
        return res.json({
          message: "Usuario creado exitosamente",
          content: resultado,
        });
      } catch (error) {
        // obtenemos el error de la ejecucion del proceso asincrono
        if (error instanceof Prisma.Prisma.PrismaClientValidationError) {
          return res.json({
            message: "error al hacer la peticion a la bd",
          });
        }
        return res.json({
          mesage: "Error al crear el usuario",
        });
      }    
});


// si una ruta va a tener masde un verbo http entonces se recomienda encapsularlas mediante el metodo route

servidor
    .route("/notas")
    .post(async (req, res) => {
        const data = req.body;
        try{
            const notaCreada = await conexion.nota.create({ data });
            
            return res.json({
                message: "Nota creada exitosamente",
                content: notaCreada,
            });
        } catch (error) {
            console.log(error)
            return res.json ({
                message: "Error al crear la nota",
            });
        }
    })
    .get(async (req, res) => {
        const notas = await conexion.nota.findMany();

        return res.json({
            content: notas,
        });
    });



servidor.listen(process.env.PORT, () => {
    console.log(
        `Servidor corriendo exitosamente en el puerto ${process.env.PORT}`
    );
});

