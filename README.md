Projeto supabase, python e Z-Api

Projeto com objetivo de enviar mensagens automáticas via WhatsApp usando contatos armazenados no Supabase e Z-API

#1º etapa Foi criado uma tabela no supabase com os seguintes requisitos: 1.id, 2.Nome, 3.Celular;

#2º etapa Foi criado um ambiente no Z-API para que possibilitasse o envio das mensagens automáticas dos cadastros feitos no Supabase; Obs.: Para o funcionamento do Z-API, utilizei o site https://us2.make.com/ para a criação de um webhook;

#3º etapa Foi necessário realizar o download das bibliotecas do python no mcd (pip install supabase e pip install requests);

#4º etapa Realização do script em IDLE-Python; Busca dos contatos da tabela ListaContatos (Nome dado para a tabela criada no supabase) no Supabase; E envio de uma mensagem via WhatsApp para cada número usando o Z-API;

#5º etapa O código foi aberto no VSCode para transferência do projeto para o GitHub
