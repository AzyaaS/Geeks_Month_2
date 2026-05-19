class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
    def earn(self):
        return "Заработал 500 донатов за 2 часа"

class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"
    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."
    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"

class GlowStreamer(Streamer, Mutant):
    # MRO: GlowStreamer -> Streamer -> Mutant -> object
    # Метод live() берётся от Streamer, потому что он первый в списке наследования
    def ultimate_content(self):
        return f"Я {self.live()} {self.superpower()} поэтому {self.earn()}"

class ViralCyborg(TikToker, Mutant):
    # MRO: ViralCyborg -> TikToker -> Mutant -> object
    def ultimate_content(self):
        return f"{Mutant.live(self)} и {TikToker.live(self)} и {self.viral()}"

class DonateMage(Streamer, TikToker):
    # MRO: DonateMage -> Streamer -> TikToker -> object
    # live() берётся от Streamer, потому что он первый в списке наследования
    def ultimate_content(self):
        return f"{self.live()}, вчера я {self.viral()} а сегодня {self.earn()}"

glow_streamer = GlowStreamer()
viral_cyborg = ViralCyborg()
donate_mage = DonateMage()

print("MRO:")
print(GlowStreamer.__mro__)
print(ViralCyborg.__mro__)
print(DonateMage.__mro__)
print()

print("live():")
print(f"GlowStreamer: {glow_streamer.live()}")
print(f"ViralCyborg: {viral_cyborg.live()}")
print(f"DonateMage: {donate_mage.live()}")
print()

print("ultimate_content:")
print(glow_streamer.ultimate_content())
print(viral_cyborg.ultimate_content())
print(donate_mage.ultimate_content())