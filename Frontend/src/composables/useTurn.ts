// Это по факту рудимент, потому что я всё-таки решил данные на сервер отправлять.
import type { Player } from '@/types/types'

export const useTurn = (player: Player) => {
  const symbol = player.order == 1 ? 'x' : 'o'
  return symbol
}
