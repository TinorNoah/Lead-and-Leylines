const CarrierConstruction = Java.loadClass('com.f22raptor.carrier.CarrierConstruction')

ItemEvents.rightClicked('kubejs:deployable_airbase', event => {
  const { level, player, item, server } = event
  if (level.isClientSide()) return

  if (!level.isOverworld()) {
    player.setStatusMessage(Text.red('The military airbase can only be deployed in the Overworld.'))
    return
  }

  if (CarrierConstruction.isBuilding(level)) {
    player.setStatusMessage(Text.yellow('Another carrier or airbase is still under construction.'))
    return
  }

  server.commands.performPrefixedCommand(
    player.createCommandSourceStack().withPermission(2),
    'f22raptor airbase'
  )
  player.addItemCooldown(item.item, 40)
  if (!player.isCreative()) {
    item.shrink(1)
  }
})
