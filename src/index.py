from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)


    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}")
    print(
        f"Olut getterit:"\
            f"\nsaldo = {olutta.saldo}"\
            f"\ntilavuus = {olutta.tilavuus}"\
            f"\npaljonko_mahtuu = {olutta.paljonko_mahtuu()}"
        )
    print("Mehu setterit:\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(
        f"Mehuvarasto: {mehua}"\
        f"\nVirhetilanteita:"\
        f"\nVarasto(-100.0);"\
        f"\n{Varasto(-100.0)}"\
        f"\nVarasto(100.0, -50.7)"\
        f"\n{Varasto(100.0, -50.7)}"\
        f"\nOlutvarasto: {olutta}"\
        f"\nolutta.lisaa_varastoon(1000.0)"
        )
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}"\
          f"\nMehuvarasto: {mehua}"\
          f"\nmehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}"\
          f"\nOlutvarasto: {olutta}"\
          f"\nnolutta.ota_varastosta(1000.0)"\
          f"\nsaatiin {olutta.ota_varastosta(1000.0)}"\
          f"\nOlutvarasto: {olutta}"\
          f"\nMehuvarasto: {mehua}"\
          f"\nmehua.otaVarastosta(-32.9)"\
          f"\nsaatiin {mehua.ota_varastosta(-32.9)}"\
          f"\nMehuvarasto: {mehua}"
          )

if __name__ == "__main__":
    main()
