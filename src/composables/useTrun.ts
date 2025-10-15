import type { Player } from '@/types/types'

export const useTurn = (player: Player) => {
  const symbol = player.order == 1 ? 'x' : 'o'
  return symbol
}
