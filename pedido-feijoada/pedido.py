class PedidoFeijoada:
    count_pedido = 0
    pedidos_concluidas = []

    def __init__(self):
        self.acompanhamento = {"Farinha": 0, "Laranja": 0, "Couve": 0, "Banana": 0}
        self.contador_acompanhamento = {
            "farinha": 0,
            "laranja": 0,
            "couve": 0,
            "banana": 0,
        }
        self.tipo_escolha = ""
        self.valor = 0
        self.qtd_feijao = 0

        PedidoFeijoada.count_pedido += 1

    def run(self):
        kwargs = self.validar_pedido()
        self.escolha_tipo_feijoada(**kwargs)
        self.informar_acapamento()
        self.criar_pedido()
        # for pedidos in PedidoFeijoada.pedidos_concluidas:
        #     for key, value in pedidos.items():
        #         print(key, value)

    def validar_pedido(self):
        while True:  # Validando o valor informado pelo úsuario
            self.qtd_feijao = int(input("informe o volume da feijoada em ml:_ "))
            if 300 <= self.qtd_feijao <= 5000:
                # calcular acréscimo do preço basico
                preco_basico = round((self.qtd_feijao / 100) * 5, 2)
                normal = preco_basico
                gourmet = round(preco_basico * 1.20)
                completa = round(preco_basico * 1.30)
                print(
                    "Normal (feijão + paio) = R$",
                    normal,
                    "\nGourmet (feijão + paio + costelinha) = R$",
                    gourmet,
                    "\nCompleta (feijão + paio + costelinha + Bacon + Pé + Orelha) = R$",
                    completa,
                )

                break
            else:
                self.lancar_erro("QUANTIDADE INVÁLIDA!")
        return {
            "normal": normal,
            "gourmet": gourmet,
            "completa": completa,
        }

    def escolha_tipo_feijoada(self, **kwargs):
        while True:
            tipo = input("Informe o tipo [N, G, C] ").lower()
            if tipo == "n" or tipo == "g" or tipo == "c":
                print(
                    "\nFarinha = R$ 2,00"
                    "\nLaranja = R$ 1,00"
                    "\nCouve refogada com bacon = R$ 3,00"
                    "\nBanana = R$ 1,00"
                )
                if tipo == "n":
                    self.tipo_escolha = "Normal"
                    self.valor = kwargs["normal"]
                elif tipo == "g":
                    self.tipo_escolha = "Gourmet"
                    self.valor = kwargs["gourmet"]
                elif tipo == "c":
                    self.tipo_escolha = "Completa"
                    self.valor = kwargs["completa"]
                break
            else:
                self.lancar_erro("TIPO INVÁLIDO!")

    def informar_acapamento(self):
        while True:
            acompanhamento = input(
                "Informe o acompanhamento [F, L, C, B, 0 = não] "
            ).lower()
            if acompanhamento == "f":
                print("Adicionado acompanhamento *Farinha* ")
                self.acompanhamento[
                    "Farinha"
                ] += 2  # incrementando o valor do preço cada vez que o úsuario adiciona um acompanhamento
                self.contador_acompanhamento["farinha"] += 1
            elif acompanhamento == "l":
                print("Adicionado acompanhamento *Laranja* ")
                self.acompanhamento["Laranja"] += 1
                self.contador_acompanhamento["laranja"] += 1
            elif acompanhamento == "c":
                print("Adicionado acompanhamento *Couve* ")
                self.acompanhamento["Couve"] += 3
                self.contador_acompanhamento["couve"] += 1
            elif acompanhamento == "b":
                print("Adicionado acompanhamento *Banana* ")
                self.acompanhamento["Banana"] += 1
                self.contador_acompanhamento["banana"] += 1
            elif (
                acompanhamento == "nao"
                or acompanhamento == "não"
                or acompanhamento == "0"
            ):
                print("***")
                break
            else:
                self.lancar_erro("acompanhamento invalido")
            continue

    def criar_pedido(self):
        farinha = ""
        laranja = ""
        couve = ""
        banana = ""
        # imprimir o acompanhamento que úsuario escolhe
        if self.contador_acompanhamento["farinha"] > 0:
            farinha = "+ farinha"
        if self.contador_acompanhamento["laranja"] > 0:
            laranja = "+ Laranja"
        if self.contador_acompanhamento["couve"] > 0:
            couve = "+ Couve"
        if self.contador_acompanhamento["banana"] > 0:
            banana = "+ banana"

        # valor total a ser pago
        preco_final = (
            self.valor
            + self.acompanhamento["Farinha"]
            + self.acompanhamento["Laranja"]
            + self.acompanhamento["Couve"]
            + self.acompanhamento["Banana"]
        )

        pedido = f"Pedido de feijoada: {self.qtd_feijao} ml de feijoada {self.tipo_escolha} {farinha} {laranja} {couve} {banana} = R$ {preco_final}"
        new_pedido = {self.count_pedido: pedido.replace("Pedido de feijoada: ", "")}
        self.pedidos_concluidas.append(new_pedido)
        print(pedido)

    def lancar_erro(self, erro):
        print(f"Error:   {erro}")


try:
    for pedido in range(10):
        my_pedido = PedidoFeijoada()
        my_pedido.run()
except KeyboardInterrupt or EOFError:
    print("\nInterrompendo a execução...")
